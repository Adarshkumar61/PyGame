import pygame as py
import sys
import numpy as np
py.init()

width, height = 800, 600
screen = py.display.set_mode((width, height))
py.display.set_caption('Circle Moving')

black = (0, 0, 0)
red = (255, 0, 0)

player_x = np.random.randint(50, 500)
player_y = np.random.randint(50, 500)
player_r = 20
player_move = 5

running = True

while running:
    py.time.delay(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_b:
                running = False
    key = py.key.get_pressed()
    if key[py.K_LEFT] and player_x - player_r > 0:
        player_x -= player_move
    if key[py.K_RIGHT] and player_x + player_r < width:
        player_x += player_move
    if key[py.K_UP] and player_y - player_r > 0:
        player_y -= player_move
    if key[py.K_DOWN] and player_y + player_r < height:
        player_y += player_move
    screen.fill(black)
    py.draw.circle(screen, red, (player_x, player_y), player_r)
    py.display.flip()
py.quit()
sys.exit()