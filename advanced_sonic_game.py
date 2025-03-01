import time
import random
import pygame
import sys

class Sonic:
    def __init__(self):
        self.rings = 0
        self.alive = True
        self.power_up = False

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

    def collect_power_up(self):
        self.power_up = True
        print("Sonic collected a power-up!")

    def encounter_enemy(self):
        if self.power_up:
            print("Sonic defeated the enemy with the power-up!")
            self.power_up = False
        elif self.rings > 0:
            self.rings -= 1
            print("Sonic encountered an enemy! Lost a ring. Total rings:", self.rings)
        else:
            self.alive = False
            print("Sonic encountered an enemy and has no rings left! Game Over.")

    def run(self):
        while self.alive:
            action = random.choice(['run', 'collect_ring', 'hit_obstacle', 'collect_power_up', 'encounter_enemy'])
            if action == 'collect_ring':
                self.collect_ring()
            elif action == 'hit_obstacle':
                self.hit_obstacle()
            elif action == 'collect_power_up':
                self.collect_power_up()
            elif action == 'encounter_enemy':
                self.encounter_enemy()
            time.sleep(1)

if __name__ == "__main__":
    sonic = Sonic()
    try:
        sonic.run()
    except KeyboardInterrupt:
        print("Game interrupted. Final ring count:", sonic.rings)

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SONIC_SPEED = 5
ENEMY_SPEED = 3
POWER_UP_DURATION = 5000  # milliseconds

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sonic the Hedgehog")

# Load Sonic image
sonic_image = pygame.image.load("sonic.png")
sonic_rect = sonic_image.get_rect()
sonic_rect.topleft = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Load Enemy image
enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.topleft = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

# Clock to control the frame rate
clock = pygame.time.Clock()

# Power-up timer
power_up_timer = 0

# Main game loop
running = True
sonic_power_up = False
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

    # Move Enemy
    if enemy_rect.x < sonic_rect.x:
        enemy_rect.x += ENEMY_SPEED
    elif enemy_rect.x > sonic_rect.x:
        enemy_rect.x -= ENEMY_SPEED

    if enemy_rect.y < sonic_rect.y:
        enemy_rect.y += ENEMY_SPEED
    elif enemy_rect.y > sonic_rect.y:
        enemy_rect.y -= ENEMY_SPEED

    # Check for collision with enemy
    if sonic_rect.colliderect(enemy_rect):
        if sonic_power_up:
            print("Sonic defeated the enemy with the power-up!")
            enemy_rect.topleft = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            sonic_power_up = False
        else:
            print("Sonic hit an enemy! Game Over.")
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw Sonic
    screen.blit(sonic_image, sonic_rect.topleft)

    # Draw Enemy
    screen.blit(enemy_image, enemy_rect.topleft)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()