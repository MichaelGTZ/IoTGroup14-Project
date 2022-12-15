import time_display
import weather_request
import pygame
from pygame import display
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import io
from urllib.request import urlopen
import requests
import cv2

pygame.init()
pygame.font.init()

green = (0, 255, 0)
blue = (0, 0, 139)
white = (255,255,255)
yellow = (255,255,102)
# Set up the drawing window
screen= display.set_mode(flags=pygame.FULLSCREEN)

# background image
# bg = pygame.image.load("background.bmp")



# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font

font_name = "/home/admin/Documents/iot_project/Roboto-Thin.ttf"
font = pygame.font.Font(font_name, 160)
font2 = pygame.font.Font(font_name, 110)
font3 = pygame.font.Font(font_name, 50)
font4 = pygame.font.Font(font_name, 50)
font5 = pygame.font.Font(font_name, 40)
font6 =  pygame.font.Font(font_name, 30)

count = 0
description, temp, feels_like, low, high, wind = weather_request.get_weather()


scope = "user-library-read,user-read-playback-position,app-remote-control,user-read-playback-state,user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

img_url = ""
outfit_msg = ""
weather_rec = ""
use_umbrella = ""

while True:
    # Fill the background with black
    screen.fill((0, 0, 0))

    time_req, day = time_display.get_datetime()
    time_req = str(time_req)
    date, time_str = time_req.split(" ")[0], time_req.split(" ")[1]
    date_obj = font2.render(date, True, white)
    time_obj = font.render(time_str, True, white)
    day = font2.render(day, True, white)

    ## spotify code
    if count % 10 == 0:
        current_song = sp.current_user_playing_track()
        # print(current_song)
        if current_song:
            if current_song['is_playing']:
                track_name = current_song['item']['name']
                artist = current_song['item']['album']['artists'][0]['name']
                img_url = current_song['item']['album']['images'][0]['url']
            else:
                img_url = ""

    if len(img_url) > 0:
        image_str = urlopen(img_url).read()
        # create a file object (stream)
        image_file = io.BytesIO(image_str)
        image = pygame.image.load(image_file)
        image = pygame.transform.scale(image, (256, 256))
        now_playing = font4.render("Now Playing", True, white)
        art = font5.render(artist, True, white)
        track = font5.render(track_name, True, white)

        screen.blit(image, (0, 1600))
        screen.blit(now_playing, (270, 1600))
        screen.blit(track, (270, 1660))
        screen.blit(art, (270, 1700))
    
    if count % 300 == 0:
        description, temp, feels_like, low, high, wind = weather_request.get_weather()
    weather_description = font2.render(description, True, white)
    curr_temperature = font.render(str(int(temp)) +chr(176), True, white)
    feels_like_temp = font3.render("Feels Like: " + str(int(feels_like)) + chr(176), True, white)
    low_temp = font3.render("Low: " + str(int(low)) + chr(176), True, white)
    high_temp = font3.render("High: " + str(int(high)) + chr(176), True, white)
    wind_speed = font3.render("Wind Speed: " + str(int(wind)) + "mph", True, white)

    if count % 10 == 0:
        cam = cv2.VideoCapture(0)
        _, frame = cam.read()
        cv2.imwrite("pic.jpg", frame)
        url = 'https://5310-34-86-196-125.ngrok.io/im_size'
        my_img = {'image': open('pic.jpg', 'rb')}
        r = requests.post(url, files=my_img)

        # convert server response into JSON format.
        r_dict = r.json()

        if int(temp) < 60 and r_dict['label'][0] != 'outerwear':
            outfit_msg = "Nice " + r_dict['label'][0] + "." 
            weather_rec = "It's cold outside, wear a jacket!"
        elif int(temp) > 75 and r_dict['label'][0] == 'outerwear':
            outfit_msg = "Nice " + r_dict['label'][0] + "."
            weather_rec = "It's hot outside, wear a t-shirt!"
        else:
            outfit_msg = "Nice " + r_dict['label'][0] + "."
            weather_rec = "That's perfect for the weather!"
        
        if "rain" in description:
            use_umbrella = "Don't forget an umbrella!"
        else:
            use_umbrella = " "
        # print(r.json())
        cam.release()
        cv2.destroyAllWindows()

    selfie = pygame.image.load('pic.jpg')
    selfie = pygame.transform.scale(selfie, (320, 180))
    screen.blit(selfie, (0, 1200))

    model_rec1 = font4.render(outfit_msg, True, white)
    model_rec2 = font4.render(weather_rec, True, white)
    model_rec3 = font4.render(use_umbrella, True, white)
    screen.blit(model_rec1, (324,1200))
    screen.blit(model_rec2, (324,1255))
    screen.blit(model_rec3, (324,1310))

    screen.blit(time_obj, (0,0))
    screen.blit(day, (0,165))
    screen.blit(date_obj, (0,280))

    screen.blit(curr_temperature, (0,500))
    screen.blit(weather_description, (0,665))
    screen.blit(high_temp, (0,790))
    screen.blit(low_temp, (300,790))
    screen.blit(feels_like_temp, (0,860))
    screen.blit(wind_speed, (0,940))

    pygame.display.update()
    sleep(1)
    count+=1
