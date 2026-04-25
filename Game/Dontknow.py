import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move the Square")

# Clock to control FPS
clock = pygame.time.Clock()

# Define square properties
square_color = (255, 0, 0)  # Red
square_size = 50
square_x = 375  # Start at center (800/2 - 50/2)
square_y = 275
square_speed = 5

# Main game loop
running = True
while running:
    screen.fill((0, 0, 255))  # Fill screen with blue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        square_x -= square_speed
    if keys[pygame.K_d]:
        square_x += square_speed
    if keys[pygame.K_w]:
        square_y -= square_speed
    if keys[pygame.K_s]:
        square_y += square_speed

    # Draw the square
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Run at 60 FPS

pygame.quit()
sys.exit()
