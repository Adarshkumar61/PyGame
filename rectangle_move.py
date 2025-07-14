import pygame as py
import numpy as np
import sys as s
py.init()

width, height = 800, 600
screen = py.display.set_mode((width, height))
py.display.set_caption('Rectangle move with arrow')

black = (0, 0, 0)
red = (255, 0, 0)
#player info:
player_x = np.random.randint(30, 500)
player_y = np.random.randint(30, 500)
player_width = 50
player_height = 50
player_movement = 5

running = True
while running:
    py.time.delay(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_b:
                running = False
            # Draw a circle instead of a rectangle
    screen.fill(black)
    key = py.key.get_pressed()
    if key[py.K_LEFT] and player_x > 0:
        player_x -= player_movement
    if key[py.K_RIGHT] and player_x < width - player_width:
        player_x += player_movement
    if key[py.K_UP] and player_y > 0:
        player_y -= player_movement
    if key[py.K_DOWN] and player_y < height - player_height:
        player_y += player_movement
    # screen.fill(black)
    py.draw.rect(screen, red, (player_x, player_y, player_width, player_height))
    py.display.flip()
    
py.quit()
s.exit()