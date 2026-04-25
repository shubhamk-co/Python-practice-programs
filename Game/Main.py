import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 255))  # Blue

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()
