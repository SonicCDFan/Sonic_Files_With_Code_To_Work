import time
import random

class Sonic:
    def __init__(self):
        self.rings = 0
        self.alive = True

    def collect_ring(self):
        self.rings += 1
        print("Sonic collected a ring! Total rings:", self.rings)

    def hit_obstacle(self):
        if self.rings > 0:
            self.rings -= 1
            print("Sonic hit an obstacle! Lost a ring. Total rings:", self.rings)
        else:
            self.alive = False
            print("Sonic hit an obstacle and has no rings left! Game Over.")

    def run(self):
        while self.alive:
            action = random.choice(['run', 'collect_ring', 'hit_obstacle'])
            if action == 'collect_ring':
                self.collect_ring()
            elif action == 'hit_obstacle':
                self.hit_obstacle()
            time.sleep(1)

if __name__ == "__main__":
    sonic = Sonic()
    try:
        sonic.run()
    except KeyboardInterrupt:
        print("Game interrupted. Final ring count:", sonic.rings)

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SONIC_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sonic the Hedgehog")

# Load Sonic image
sonic_image = pygame.image.load("sonic.png")
sonic_rect = sonic_image.get_rect()
sonic_rect.topleft = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Move Sonic
    if keys[pygame.K_LEFT]:
        sonic_rect.x -= SONIC_SPEED
    if keys[pygame.K_RIGHT]:
        sonic_rect.x += SONIC_SPEED
    if keys[pygame.K_UP]:
        sonic_rect.y -= SONIC_SPEED
    if keys[pygame.K_DOWN]:
        sonic_rect.y += SONIC_SPEED

    # Prevent Sonic from going off-screen
    if sonic_rect.left < 0:
        sonic_rect.left = 0
    if sonic_rect.right > SCREEN_WIDTH:
        sonic_rect.right = SCREEN_WIDTH
    if sonic_rect.top < 0:
        sonic_rect.top = 0
    if sonic_rect.bottom > SCREEN_HEIGHT:
        sonic_rect.bottom = SCREEN_HEIGHT

    # Clear the screen
    screen.fill(WHITE)

    # Draw Sonic
    screen.blit(sonic_image, sonic_rect.topleft)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
