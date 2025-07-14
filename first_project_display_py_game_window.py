import pygame as py
import sys

py.init()

screen_width = 800
screen_height = 600

screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption('my first pygame winodow')

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_b:
                running = False
    screen.fill((0,255, 255))
    py.display.flip()
py.quit()
sys.exit()