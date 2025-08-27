# import pygame as py
# import sys
# import numpy as  np
# import math
# import cv2 as cv


# def cam():
#     cam = cv.VideoCapture(0)
#     while True: 
#        ret, frame = cam.read()
#        if not ret:
#            print('frame not capturing')
#            break
#        cv.imshow('frame', frame)
#        if cv.waitKey(1) & 0xFF == ord('b'):
#            break
       
#     cam.release()
#     cv.destroyAllWindows()

# py.init()
# WIDTH = 800
# HEIGHT = 600

# screen = py.display.set_mode((WIDTH, HEIGHT))
# py.display.set_caption('Player_vs enemy')
# black = (0, 0, 0)
# blue = (0, 0, 255)
# red = (255, 0, 0)

# # enemy:
# enemy_x = np.random.randint(50, 500)
# enemy_y = np.random.randint(50, 150)
# enemy_w = 50
# enemy_h = 50

# # player:
# player_x = np.random.randint(50, 150)
# player_y = np.random.randint(50, 150)
# player_r = 25
# player_m  = 5

# running = True
# collision = False
# while running:
#     py.time.delay(10)
#     for event in py.event.get():
#         if event.type ==  py.QUIT:
#             running = False
#         elif event.type == py.KEYDOWN:
#             if event.key == py.K_b:
#                 running = False
#     key = py.key.get_pressed()
#     if key[py.K_LEFT] and player_x - player_r > 0:
#         player_x -= player_m
#     if key[py.K_RIGHT] and player_x + player_r <  WIDTH:
#         player_x += player_m
#     if key[py.K_UP] and player_y - player_r > 0:
#         player_y -= player_m
#     if key[py.K_DOWN]  and player_y + player_r < HEIGHT:
#         player_y += player_m
    
#     screen.fill(black)
#     py.draw.circle(screen, blue, (player_x, player_y), player_r)
#     py.draw.rect(screen, red, (enemy_x, enemy_y, enemy_w, enemy_h))
#     closest_x = max(enemy_x, min(player_x, enemy_x + enemy_w))
#     closest_y = max(enemy_y, min(player_y, enemy_y + enemy_h))

#     # Step 2: Calculate distance from circle center to that point
#     dx = player_x - closest_x
#     dy = player_y - closest_y
#     distancenemy_squared = dx * dx + dy * dy
#     if distancenemy_squared <= player_r * player_r and not collision:
#         print("Collision!")
#         collision = True
#         cam()  # Open camera when collision occurs
#         running = False
#     # distance = math.hypot(enemy_x - c_x, enemy_y - c_y)
#     # if distance <= c_r + (enemy_x+ enemy_y):
#     #     print('collision')
#     py.display.flip()
    
# py.quit()
# sys.exit()


# this is code of player vs enemy where:
# player is rectange
# enemy is circle

import numpy as np
import sys
import pygame as py

py.init()

width = 800
height = 600

screen = py.display.set_mode((width, height))
py.display.set_caption('Player_enemy')

# color:
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#player:
p_x = np.random.randint(50, 550)
p_y = np.random.randint(50, 550)
p_h = 50
p_w = 50
p_m = 5

# enemy:
e_x = np.random.randint(50, 550)
e_y = np.random.randint(50, 550)
e_r = 25
e_m = 5
running = True
while running:
    py.time.delay(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_b:
                running = False
    
    key = py.key.get_pressed()
    # Simple enemy movement: move towards the player
    if e_x < p_x:
        e_x += e_m
    if e_x > p_x:
        e_x -= e_m
    if e_y < p_y:
        e_y += e_m
    if e_y > p_y:
        e_y -= e_m
    if key[py.K_LEFT] and p_x > 0:
        p_x -= p_m
    if key[py.K_RIGHT] and p_x + p_w < width:
        p_x += p_m
    if key[py.K_UP] and p_y > 0:
        p_y-= p_m 
    if key[py.K_DOWN] and p_y + p_h < height:
        p_y += p_m
    
    screen.fill(black)
    py.draw.rect(screen, blue, (p_x, p_y, p_w, p_h), border_top_left_radius= 10, border_bottom_right_radius= 10)
    py.draw.circle(screen, red,(e_x, e_y), e_r)
    
    closest_x = max(p_x, min(e_x, p_x + p_w))
    closest_y = max(p_y, min(e_y, p_y + p_h))
    
    dx = e_x - closest_x
    dy = e_y - closest_y
    
    sq = dx * dx + dy * dy
    if sq <= e_r * e_r:
        print('Collision Happened')
        running = False
    py.display.flip()

py.quit()
sys.exit()