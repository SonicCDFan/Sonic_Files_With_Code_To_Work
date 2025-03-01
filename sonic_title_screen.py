import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sonic Simulator")

# Load Sonic logo image
logo_image = pygame.image.load("sonic_logo.png")
logo_rect = logo_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))

# Create title card
font = pygame.font.Font(None, 74)
title_card = font.render("Sonic Simulator", True, BLUE)
title_card_rect = title_card.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Create start game text
start_text = font.render("Press Enter to Start", True, BLACK)
start_text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Start the game
                running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw logo and title card
    screen.blit(logo_image, logo_rect)
    screen.blit(title_card, title_card_rect)
    screen.blit(start_text, start_text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 74

def load_image(path):
    try:
        return pygame.image.load(path)
    except pygame.error as e:
        print(f"Unable to load image at {path}: {e}")
        sys.exit()

def create_text(text, color, size, center):
    font = pygame.font.Font(None, size)
    rendered_text = font.render(text, True, color)
    return rendered_text, rendered_text.get_rect(center=center)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sonic the Hedgehog")

# Load Sonic logo image
logo_image = load_image("sonic_logo.png")
logo_rect = logo_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))

# Create title card and start game text
title_card, title_card_rect = create_text("Sonic the Hedgehog", BLUE, FONT_SIZE, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
start_text, start_text_rect = create_text("Press Enter to Start", BLACK, FONT_SIZE, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Start the game
                running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw logo and title card
    screen.blit(logo_image, logo_rect)
    screen.blit(title_card, title_card_rect)
    screen.blit(start_text, start_text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
