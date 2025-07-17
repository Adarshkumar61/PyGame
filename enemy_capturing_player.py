import pygame as py
import numpy as np
import math
import sys

py.init()

width, height = 800, 600

screen = py.display.set_mode((width, height))
py.display.set_caption('Player_Vs Enemy')

# color:
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# player:
p_x = np.random.randint(50, 550)
p_y = np.random.randint(50, 550)
p_w = 40
p_h = 40
p_s = 5

# enemy:
e_x = np.random.randint(50, 550)
e_y = np.random.randint(50, 550)
e_r = 23
e_s = 2

running = True
while running:
    py.time.delay(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    key = py.key.get_pressed()
    
    if key[py.K_LEFT] and p_x > 0:
        p_x -= p_s
    
    if key[py.K_RIGHT] and p_x + p_w < width:
        p_x += p_s
        
    if key[py.K_UP] and p_y > 0:
        p_y -= p_s
    
    if key[py.K_DOWN] and p_y + p_h < height:
        p_y += p_s
        
    # get player center:
    p_center_x = p_x + p_w //2
    p_center_y = p_y + p_h //2
    
    #get direction vector:
    
    dx = p_center_x - e_x 
    dy = p_center_y - e_y
    
    ds = math.hypot(dx, dy)
    
    if ds != 0:
        dx /= ds
        dy /= ds
        e_x += dx * e_s
        e_y+= dy * e_s
        
    # closest point on rectangle
    closest_x = max(p_x, min(e_x, p_x + p_w))
    closest_y = max(p_y, min(e_y, p_y + p_h))
    
    
    distance_x = e_x - closest_x
    distance_y = e_x - closest_y
    ds = distance_x**2 + distance_y ** 2
    
    if ds <= e_r ** 2:
        print('Collision')
        running = False
    screen.fill(black)
    
    py.draw.rect(screen, green, (p_x, p_y, p_w, p_h))
    py.draw.circle(screen, red, (e_x, e_y), e_r)
    
    py.display.flip()
py.quit()
sys.exit()
    