import time_display
import weather_request
# Import and initialize the pygame library
import pygame
from pygame import display
import time

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


font = pygame.font.SysFont('consolas', 160)
font2 = pygame.font.SysFont('consolas', 110)
font3 = pygame.font.SysFont('consolas', 50)

count = 0
description, temp, feels_like, low, high, wind = weather_request.get_weather()
while True:
    time_req, day = time_display.get_datetime()
    time_req = str(time_req)
    date, time_str = time_req.split(" ")[0], time_req.split(" ")[1]
    date_obj = font2.render(date, True, white)
    time_obj = font.render(time_str, True, white)
    day = font2.render(day, True, white)

    
    if(count%300 == 0):
        description, temp, feels_like, low, high, wind = weather_request.get_weather()
    weather_description = font2.render(description, True, white)
    curr_temperature = font.render(str(int(temp)) +chr(176), True, white)
    feels_like_temp = font3.render("Feels Like: " + str(int(feels_like)) + chr(176), True, white)
    low_temp = font3.render("Low: " + str(int(low)) + chr(176), True, white)
    high_temp = font3.render("High: " + str(int(high)) + chr(176), True, white)
    wind_speed = font3.render("Wind Speed: " + str(int(wind)) + "mph", True, white)

    # Fill the background with black
    screen.fill((0, 0, 0))
    # screen.blit(bg, (0, 0))


    screen.blit(time_obj, (0,0))
    screen.blit(day, (0,165))
    screen.blit(date_obj, (0,280))

    screen.blit(curr_temperature, (0,500))
    screen.blit(weather_description, (0,665))
    screen.blit(high_temp, (0,780))
    screen.blit(low_temp, (300,780))
    screen.blit(feels_like_temp, (0,860))
    screen.blit(wind_speed, (0,940))

    pygame.display.update()
    time.sleep(1)
    count+=1
