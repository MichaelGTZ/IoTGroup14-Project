import time_display
import weather_request
# Import and initialize the pygame library
import pygame
from pygame import display
import cv2

pygame.init()
pygame.font.init()

green = (0, 255, 0)
blue = (0, 0, 128)
# Set up the drawing window
screen= display.set_mode(flags=pygame.RESIZABLE)


font = pygame.font.SysFont('Arial', 72)

# set up camera\
cap = cv2.VideoCapture(0)
_, frame = cap.read()

cv2.imwrite("pic.jpg", frame)

while True:
    time_req = str(time_display.get_datetime())
    curr_time = font.render(time_req, True, green)

    description, temp = weather_request.get_weather()
    weather_description = font.render(description, True, green)
    curr_temperature = font.render(temp, True, green)


    # Fill the background with black
    screen.fill((0, 0, 0))

    screen.blit(curr_time, (0,0))
    screen.blit(weather_description, (0,80))
    screen.blit(curr_temperature, (0,160))
    pygame.display.update()
