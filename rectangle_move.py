import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move Rectangle with Arrow Keys")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define player size and position
player_x = 100
player_y = 100
player_width = 50
player_height = 50
player_speed = 5  # Speed of movement

# Game loop
running = True
while running:
    pygame.time.wait(5)  # Small delay to slow down movement

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states (which keys are currently pressed)
    keys = pygame.key.get_pressed()

    # Move player based on key input
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
        player_y += player_speed

    # Fill screen background
    screen.fill(WHITE)

    # Draw the player rectangle
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.flip()

# Quit game
pygame.quit()
sys.exit()
