# import pygame as py 
# import sys

# py.init()

# screen_width = 800
# screen_height = 600

# screen = py.display.set_mode((screen_width, screen_height))
# py.display.set_caption('my first window')

# running = True
# while running:
#     for event in py.event.get():
#         if event.type == py.QUIT:
#             running = False
#     screen.fill((155, 120, 255))
#     py.display.flip()
    
# py.quit()
# sys.exit()

#rectange movement:
# import pygame
# import sys
# import numpy as np

# # Initialize pygame
# pygame.init()

# # Set screen dimensions
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Move Rectangle with Arrow Keys")

# # Define colors
# Black = (0, 0, 0)
# RED = (255, 0, 0)

# # Define player size and position
# player_x = np.random.randint(20, 500) 
# player_y = np.random.randint(20, 500)
# player_width = 50
# player_height = 50
# player_speed = 5  # Speed of movement

# # Game loop
# running = True
# while running:
#     pygame.time.delay(10)  # Small delay to slow down movement

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Get key states (which keys are currently pressed)
#     keys = pygame.key.get_pressed()

#     # Move player based on key input
#     if keys[pygame.K_LEFT] and player_x > 0:
#         player_x -= player_speed
#     if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
#         player_x += player_speed
#     if keys[pygame.K_UP] and player_y > 0:
#         player_y -= player_speed
#     if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
#         player_y += player_speed

#     # Fill screen background
#     screen.fill(Black)

#     # Draw the player rectangle
#     pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

#     # Update the display
#     pygame.display.flip()

# # Quit game
# pygame.quit()
# sys.exit()


# circle movement:
# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set screen dimensions
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Move Circle with Arrow Keys")

# # Colors
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)

# # Circle properties
# circle_x = 100  # X position of circle center
# circle_y = 100  # Y position of circle center
# circle_radius = 25  # Radius of the circle
# circle_speed = 5

# # Game loop
# running = True
# while running:
#     pygame.time.delay(10)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Get keys
#     keys = pygame.key.get_pressed()

#     # Movement with border conditions
#     if keys[pygame.K_LEFT] and circle_x - circle_radius > 0:
#         circle_x -= circle_speed
#     if keys[pygame.K_RIGHT] and circle_x + circle_radius < WIDTH:
#         circle_x += circle_speed
#     if keys[pygame.K_UP] and circle_y - circle_radius > 0:
#         circle_y -= circle_speed
#     if keys[pygame.K_DOWN] and circle_y + circle_radius < HEIGHT:
#         circle_y += circle_speed

#     # Fill background
#     screen.fill(WHITE)

#     # Draw circle
#     pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)

#     # Update display
#     pygame.display.flip()

# # Exit
# pygame.quit()
# sys.exit()

# import pygame as py
# import sys
# import numpy as np
# import cv2 as cv

# def cam():
#     cam = cv.VideoCapture(0)
#     if not cam.isOpened():
#         print("Camera not found")
#         return

#     while True:
#         ret, frame = cam.read()
#         if not ret:
#             print("Can't receive frame. Exiting...")
#             break

#         cv.imshow('Camera - Press b to close', frame)

#         # Wait for 'b' key to break
#         key = cv.waitKey(1) & 0xFF
#         if key == ord('b'):
#             break

#     cam.release()
#     cv.destroyAllWindows()

# Initialize pygame
# py.init()
# WIDTH, HEIGHT = 800, 600
# screen = py.display.set_mode((WIDTH, HEIGHT))
# py.display.set_caption('Player vs Enemy')

# # Colors
# BLACK = (0, 0, 0)
# BLUE = (0, 0, 255)
# RED = (255, 0, 0)

# # Player (Circle)
# c_x = 100
# c_y = 100
# c_r = 25
# c_m = 5

# # Enemy (Rectangle)
# e_x = 400
# e_y = 300
# e_w = 100
# e_h = 80

# running = True
# collision_happened = False  # To make sure camera opens only once

# while running:
#     py.time.delay(10)

#     for event in py.event.get():
#         if event.type == py.QUIT:
#             running = False

#     keys = py.key.get_pressed()
#     if keys[py.K_LEFT] and c_x - c_r > 0:
#         c_x -= c_m
#     if keys[py.K_RIGHT] and c_x + c_r < WIDTH:
#         c_x += c_m
#     if keys[py.K_UP] and c_y - c_r > 0:
#         c_y -= c_m
#     if keys[py.K_DOWN] and c_y + c_r < HEIGHT:
#         c_y += c_m

#     # Drawing
#     screen.fill(BLACK)
#     py.draw.circle(screen, BLUE, (c_x, c_y), c_r)
#     py.draw.rect(screen, RED, (e_x, e_y, e_w, e_h))

#     # Collision Detection (circle vs rectangle)
#     closest_x = max(e_x, min(c_x, e_x + e_w))
#     closest_y = max(e_y, min(c_y, e_y + e_h))
#     dx = c_x - closest_x
#     dy = c_y - closest_y
#     distance_squared = dx * dx + dy * dy

#     if distance_squared <= c_r * c_r and not collision_happened:
#         print("Collision Detected!")
#         collision_happened = True  # prevent calling cam() repeatedly
#         cam()
#         running = False  # exit the game after camera closes

#     py.display.flip()

# # Quit Pygame
# py.quit()
# sys.exit()

# import pygame as py
# import sys
# import math

# # Initialize
# py.init()
# WIDTH, HEIGHT = 800, 600
# screen = py.display.set_mode((WIDTH, HEIGHT))
# py.display.set_caption("Enemy Movement + Collision")

# # Colors
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)     # Player
# GREEN = (0, 255, 0)   # Enemy

# # Player (rectangle)
# player_x = 100
# player_y = 100
# player_w = 50
# player_h = 50
# player_speed = 5

# # Enemy (circle)
# enemy_x = 600
# enemy_y = 400
# enemy_radius = 25
# enemy_speed = 2

# # Game loop
# running = True
# while running:
#     py.time.delay(10)

#     for event in py.event.get():
#         if event.type == py.QUIT:
#             running = False

#     # Player movement
#     keys = py.key.get_pressed()
#     if keys[py.K_LEFT] and player_x > 0:
#         player_x -= player_speed
#     if keys[py.K_RIGHT] and player_x + player_w < WIDTH:
#         player_x += player_speed
#     if keys[py.K_UP] and player_y > 0:
#         player_y -= player_speed
#     if keys[py.K_DOWN] and player_y + player_h < HEIGHT:
#         player_y += player_speed

#     # ---------------- Enemy moves toward player ----------------
#     # Get player center
#     player_center_x = player_x + player_w // 2
#     player_center_y = player_y + player_h // 2

#     # Get direction vector
#     dx = player_center_x - enemy_x
#     dy = player_center_y - enemy_y
#     distance = math.hypot(dx, dy)

#     # Normalize direction and move enemy
#     if distance != 0:
#         dx /= distance
#         dy /= distance
#         enemy_x += dx * enemy_speed
#         enemy_y += dy * enemy_speed

#     # ---------------- Collision Detection ----------------
#     # Find closest point on player rect to enemy center
#     closest_x = max(player_x, min(enemy_x, player_x + player_w))
#     closest_y = max(player_y, min(enemy_y, player_y + player_h))

#     dist_x = enemy_x - closest_x
#     dist_y = enemy_y - closest_y
#     dist_squared = dist_x ** 2 + dist_y ** 2

#     if dist_squared <= enemy_radius ** 2:
#         print("Hit!")
#         running = False

#     # ---------------- Drawing ----------------
#     screen.fill(BLACK)
#     py.draw.rect(screen, RED, (player_x, player_y, player_w, player_h))
#     py.draw.circle(screen, GREEN, (int(enemy_x), int(enemy_y)), enemy_radius)
#     py.display.flip()

# py.quit()
# sys.exit()


# import pygame as py
# import sys
# import math

# # Init
# py.init()
# WIDTH, HEIGHT = 800, 600
# screen = py.display.set_mode((WIDTH, HEIGHT))
# py.display.set_caption("Shooting + Enemy Hit")

# # Colors
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)     # Player
# GREEN = (0, 255, 0)   # Enemy
# BLUE = (0, 0, 255)    # Bullet

# # Player (Rectangle)
# player_x = 100
# player_y = 500
# player_w = 50
# player_h = 50
# player_speed = 5

# # Enemy (Circle)
# enemy_x = 400
# enemy_y = 100
# enemy_radius = 30

# # Bullets (each bullet is [x, y])
# bullets = []
# bullet_speed = 7

# running = True
# while running:
#     py.time.delay(10)

#     for event in py.event.get():
#         if event.type == py.QUIT:
#             running = False
#         # Shoot bullet on SPACE key
#         if event.type == py.KEYDOWN:
#             if event.key == py.K_SPACE:
#                 # Spawn bullet from center of player top
#                 bullet_x = player_x + player_w // 2
#                 bullet_y = player_y
#                 bullets.append([bullet_x, bullet_y])

#     # Player Movement
#     keys = py.key.get_pressed()
#     if keys[py.K_LEFT] and player_x > 0:
#         player_x -= player_speed
#     if keys[py.K_RIGHT] and player_x + player_w < WIDTH:
#         player_x += player_speed
#     if keys[py.K_UP] and player_y > 0:
#         player_y -= player_speed
#     if keys[py.K_DOWN] and player_y + player_h < HEIGHT:
#         player_y += player_speed

#     # Move bullets upward
#     for bullet in bullets:
#         bullet[1] -= bullet_speed

#     # Remove bullets off screen
#     bullets = [b for b in bullets if b[1] > 0]

#     # Collision: Bullet hits enemy
#     for bullet in bullets:
#         dist_x = bullet[0] - enemy_x
#         dist_y = bullet[1] - enemy_y
#         distance = math.hypot(dist_x, dist_y)
#         if distance <= enemy_radius:
#             print("Enemy Hit!")
#             bullets.remove(bullet)  # Remove bullet on hit
            

#     # Draw
#     screen.fill(BLACK)
#     py.draw.rect(screen, RED, (player_x, player_y, player_w, player_h))
#     py.draw.circle(screen, GREEN, (enemy_x, enemy_y), enemy_radius)
#     for bullet in bullets:                
#         py.draw.circle(screen, BLUE, (int(bullet[0]), int(bullet[1])), 5)

#     py.display.flip()

# py.quit()
# sys.exit()


<<<<<<< HEAD
# import pygame as py
# import sys
# import math
# import random

# # Init
# py.init()
# WIDTH, HEIGHT = 800, 600
# screen = py.display.set_mode((WIDTH, HEIGHT))
# py.display.set_caption("Shooting Game - Player vs Enemy")

# # Colors
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)     # Player
# GREEN = (0, 255, 0)   # Enemy
# BLUE = (0, 0, 255)    # Player Bullet
# YELLOW = (255, 255, 0) # Enemy Bullet
# WHITE = (255, 255, 255)

# # Fonts
# font = py.font.SysFont("Arial", 24)

# # Player (Rectangle)
# player_x = 100
# player_y = 500
# player_w = 50
# player_h = 50
# player_speed = 5

# # Enemy (Circle)
# enemy_x = 400
# enemy_y = 100
# enemy_radius = 30
# enemy_speed = 2

# # Bullets
# player_bullets = []     # [x, y]
# enemy_bullets = []      # [x, y]
# bullet_speed = 7
# enemy_bullet_speed = 4
# enemy_fire_delay = 60   # frames between shots
# enemy_fire_timer = 0

# # Score
# score = 0

# running = True
# while running:
#     py.time.delay(10)
#     screen.fill(BLACK)

#     for event in py.event.get():
#         if event.type == py.QUIT:
#             running = False
#         # Player fires
#         if event.type == py.KEYDOWN:
#             if event.key == py.K_SPACE:
#                 bullet_x = player_x + player_w // 2
#                 bullet_y = player_y
#                 player_bullets.append([bullet_x, bullet_y])

#     # Player Movement
#     keys = py.key.get_pressed()
#     if keys[py.K_LEFT] and player_x > 0:
#         player_x -= player_speed
#     if keys[py.K_RIGHT] and player_x + player_w < WIDTH:
#         player_x += player_speed
#     if keys[py.K_UP] and player_y > 0:
#         player_y -= player_speed
#     if keys[py.K_DOWN] and player_y + player_h < HEIGHT:
#         player_y += player_speed

#     # --------- Player Bullets ---------
#     for b in player_bullets:
#         b[1] -= bullet_speed
#     player_bullets = [b for b in player_bullets if b[1] > 0]

#     # Collision with Enemy
#     for b in player_bullets:
#         dx = b[0] - enemy_x
#         dy = b[1] - enemy_y
#         if math.hypot(dx, dy) <= enemy_radius:
#             print("Enemy Hit!")
#             player_bullets.remove(b)
#             score += 10

#     # --------- Enemy Shoots Back ---------
#     enemy_fire_timer += 1
#     if enemy_fire_timer >= enemy_fire_delay:
#         # Shoot toward player
#         bullet_x = enemy_x
#         bullet_y = enemy_y
#         enemy_bullets.append([bullet_x, bullet_y])
#         enemy_fire_timer = 0

#     # Move Enemy Bullets Down
#     for b in enemy_bullets:
#         b[1] += enemy_bullet_speed
#     enemy_bullets = [b for b in enemy_bullets if b[1] < HEIGHT]

#     # Collision with Player
#     for b in enemy_bullets:
#         if (player_x < b[0] < player_x + player_w) and (player_y < b[1] < player_y + player_h):
#             print("Player Hit!")
#             enemy_bullets.remove(b)

#     # --------- Draw Everything ---------
#     # Player
#     py.draw.rect(screen, RED, (player_x, player_y, player_w, player_h))

#     # Enemy
#     py.draw.circle(screen, GREEN, (enemy_x, enemy_y), enemy_radius)

#     # Player Bullets
#     for b in player_bullets:
#         py.draw.circle(screen, BLUE, (int(b[0]), int(b[1])), 5)

#     # Enemy Bullets
#     for b in enemy_bullets:
#         py.draw.circle(screen, YELLOW, (int(b[0]), int(b[1])), 5)

#     # Score
#     score_text = font.render(f"Score: {score}", True, WHITE)
#     screen.blit(score_text, (10, 10))

#     py.display.flip()

# py.quit()
# sys.exit()

import pygame as py
import sys
py.init()

height = 600
width = 800

screen = py.display.set_mode((width, height))
py.display.set_caption('window')


player_x = 21
player_y = 21
p_width = 20
p_height = 40
p_speed = 20
running = True
while running:
    py.time.delay(10)  # Delay to control frame rate
    for event in py.event.get():
        
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_LEFT and player_x > 0:
                player_x -= p_speed
            elif event.key == py.K_RIGHT and player_x < width - p_width:
                player_x += p_speed
            elif event.key == py.K_UP and player_y > 0:
                player_y -= p_speed
            elif event.key == py.K_DOWN and player_y < height - p_height:
                player_y += p_speed

    screen.fill((0, 0, 0))  # Clear the screen with black
    py.draw.rect(screen, (255, 0, 0), (player_x, player_y, p_width, p_height))  # Draw the player rectangle
    py.display.flip()  # Update the display 
sys.exit()
=======
import pygame as py
import sys
import math
import random

# Init
py.init()
WIDTH, HEIGHT = 800, 600
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Shooting Game - Player vs Enemy")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)     # Player
GREEN = (0, 255, 0)   # Enemy
BLUE = (0, 0, 255)    # Player Bullet
YELLOW = (255, 255, 0) # Enemy Bullet
WHITE = (255, 255, 255)

# Fonts
font = py.font.SysFont("Arial", 24)

# Player (Rectangle)
player_x = 100
player_y = 500
player_w = 50
player_h = 50
player_speed = 5

# Enemy (Circle)
enemy_x = 400
enemy_y = 100
enemy_radius = 30
enemy_speed = 2

# Bullets
player_bullets = []     # [x, y]
enemy_bullets = []      # [x, y]
bullet_speed = 7
enemy_bullet_speed = 4
enemy_fire_delay = 60   # frames between shots
enemy_fire_timer = 0

# Score
score = 0

running = True
while running:
    py.time.delay(10)
    screen.fill(BLACK)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        # Player fires
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                bullet_x = player_x + player_w // 2
                bullet_y = player_y
                player_bullets.append([bullet_x, bullet_y])

    # Player Movement
    keys = py.key.get_pressed()
    if keys[py.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[py.K_RIGHT] and player_x + player_w < WIDTH:
        player_x += player_speed
    if keys[py.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[py.K_DOWN] and player_y + player_h < HEIGHT:
        player_y += player_speed

    # --------- Player Bullets ---------
    for b in player_bullets:
        b[1] -= bullet_speed
    player_bullets = [b for b in player_bullets if b[1] > 0]

    # Collision with Enemy
    for b in player_bullets:
        dx = b[0] - enemy_x
        dy = b[1] - enemy_y
        if math.hypot(dx, dy) <= enemy_radius:
            print("Enemy Hit!")
            player_bullets.remove(b)
            score += 10

    # --------- Enemy Shoots Back ---------
    enemy_fire_timer += 1
    if enemy_fire_timer >= enemy_fire_delay:
        # Shoot toward player
        bullet_x = enemy_x
        bullet_y = enemy_y
        enemy_bullets.append([bullet_x, bullet_y])
        enemy_fire_timer = 0

    # Move Enemy Bullets Down
    for b in enemy_bullets:
        b[1] += enemy_bullet_speed
    enemy_bullets = [b for b in enemy_bullets if b[1] < HEIGHT]

    # Collision with Player
    for b in enemy_bullets:
        if (player_x < b[0] < player_x + player_w) and (player_y < b[1] < player_y + player_h):
            print("Player Hit!")
            enemy_bullets.remove(b)

    # --------- Draw Everything ---------
    # Player
    py.draw.rect(screen, RED, (player_x, player_y, player_w, player_h))

    # Enemy
    py.draw.circle(screen, GREEN, (enemy_x, enemy_y), enemy_radius)

    # Player Bullets
    for b in player_bullets:
        py.draw.circle(screen, BLUE, (int(b[0]), int(b[1])), 5)

    # Enemy Bullets
    for b in enemy_bullets:
        py.draw.circle(screen, YELLOW, (int(b[0]), int(b[1])), 5)

    # Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    py.display.flip()

py.quit()
sys.exit()
>>>>>>> ec0bb87fd85222af99c9f74adaabc2e021cdf159
