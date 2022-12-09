import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep


# export SPOTIPY_REDIRECT_URI=https://open.spotify.com/
# export SPOTIPY_CLIENT_ID=582fcc43942c4cb783378bafde3c54de
# export SPOTIPY_CLIENT_SECRET=afc35b68387b4198b0539c394a36b2ad

scope = "user-library-read,user-read-playback-position,app-remote-control,user-read-playback-state,user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

counter = 0
while True:
    # Check if song is playing every 10 seconds, can maybe do this smarter using song dura+prog
    # But user skipping songs or scrubbing could throw this off
    if counter % 10 == 0:
        current_song = sp.current_user_playing_track()
        print(list(current_song['item']['album'].keys()))
        track_prog = current_song['progress_ms']
        track_dura = current_song['item']['duration_ms']
        track_name = current_song['item']['name']
        artist = current_song['item']['album']['artists'][0]['name']
        img_url = current_song['item']['album']['images'][0]['url']
        print(track_name, artist, img_url)
        pass
    sleep(1)
    counter+=1