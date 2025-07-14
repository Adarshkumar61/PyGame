import pygame as py
import numpy as np
import sys as s
py.init()

width, height = 800, 600
screen = py.display.set_mode((width, height))
py.display.set_caption('Rectangle move with arrow')

#player info:
player_x = np.random.randint(30, 500)
player_y = np.random.randint(30, 500)
player_width = 50
player_height = 50
player_movement = 5