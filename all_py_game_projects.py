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

def cam():
    cam = cv.VideoCapture(0)
    if not cam.isOpened():
        print("Camera not found")
        return

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Can't receive frame. Exiting...")
            break

        cv.imshow('Camera - Press b to close', frame)

        # Wait for 'b' key to break
        key = cv.waitKey(1) & 0xFF
        if key == ord('b'):
            break

    cam.release()
    cv.destroyAllWindows()

# Initialize pygame
py.init()
WIDTH, HEIGHT = 800, 600
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption('Player vs Enemy')

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player (Circle)
c_x = 100
c_y = 100
c_r = 25
c_m = 5

# Enemy (Rectangle)
e_x = 400
e_y = 300
e_w = 100
e_h = 80

running = True
collision_happened = False  # To make sure camera opens only once

while running:
    py.time.delay(10)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    keys = py.key.get_pressed()
    if keys[py.K_LEFT] and c_x - c_r > 0:
        c_x -= c_m
    if keys[py.K_RIGHT] and c_x + c_r < WIDTH:
        c_x += c_m
    if keys[py.K_UP] and c_y - c_r > 0:
        c_y -= c_m
    if keys[py.K_DOWN] and c_y + c_r < HEIGHT:
        c_y += c_m

    # Drawing
    screen.fill(BLACK)
    py.draw.circle(screen, BLUE, (c_x, c_y), c_r)
    py.draw.rect(screen, RED, (e_x, e_y, e_w, e_h))

    # Collision Detection (circle vs rectangle)
    closest_x = max(e_x, min(c_x, e_x + e_w))
    closest_y = max(e_y, min(c_y, e_y + e_h))
    dx = c_x - closest_x
    dy = c_y - closest_y
    distance_squared = dx * dx + dy * dy

    if distance_squared <= c_r * c_r and not collision_happened:
        print("Collision Detected!")
        collision_happened = True  # prevent calling cam() repeatedly
        cam()
        running = False  # exit the game after camera closes

    py.display.flip()

# Quit Pygame
py.quit()
sys.exit()

