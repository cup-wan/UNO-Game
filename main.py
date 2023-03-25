import pygame, os
from button import Button
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Define constants and colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_FONT = pygame.font.Font(None, 36)
TITLE_FONT = pygame.font.Font(None, 72)

# Create a Pygame window and set its caption
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("UNO GAME")
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
icon = pygame.image.load(os.path.join(image_path, "title_image.png"))
pygame.display.set_icon(icon)

# Define the title text and font
title_text = "UNO"
title_surface = TITLE_FONT.render(title_text, True, BLACK)
title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))

# Create three Button instances for the start page
start_button = Button(0.5, 0.5, 0.3, 0.1, "Start", button_color=GREEN)
settings_button = Button(0.5, 0.65, 0.3, 0.1, "Settings", button_color=BLUE)
exit_button = Button(0.5, 0.8, 0.3, 0.1, "Exit", button_color=RED)

def update_title_text():
    global title_surface, title_rect
    screen_width, screen_height = pygame.display.get_surface().get_size()
    title_surface = TITLE_FONT.render(title_text, True, BLACK)
    title_rect = title_surface.get_rect(center=(screen_width // 2, screen_height // 6))

def change_window_size(size):
    global screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("UNO Start Page")
    start_button.update_size()
    settings_button.update_size()
    exit_button.update_size()
    update_title_text()

def settings_screen():
    # Create four Button instances for the settings screen
    window_size_button = Button(0.5, 0.3, 0.4, 0.1, "Window Size", button_color=BLUE, text_color=WHITE)
    key_setting_button = Button(0.5, 0.45, 0.4, 0.1, "Key Setting", button_color=BLUE, text_color=WHITE)
    color_weakness_button = Button(0.5, 0.6, 0.4, 0.1, "Color Weakness Mode", button_color=BLUE, text_color=WHITE)
    default_button = Button(0.5, 0.75, 0.4, 0.1, "Default", button_color=BLUE, text_color=WHITE)
    back_button = Button(0.5, 0.9, 0.4, 0.1, "Back", button_color=BLUE, text_color=WHITE)

    # Window sizes
    window_sizes = [(640, 480), (800, 600), (1280, 720)]
    window_size_index = 0

    running = True
    while running:
        screen.fill(WHITE)

        # Handle events 
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

            # Check for button clicks
            if window_size_button.handle_event(event):
                print("Window Size button clicked")
                window_size_index = (window_size_index + 1) % len(window_sizes)
                change_window_size(window_sizes[window_size_index])
                window_size_button.text = f"Window Size: {window_sizes[window_size_index][0]}x{window_sizes[window_size_index][1]}"
                window_size_button.update_size()
            if key_setting_button.handle_event(event):
                print("Key Setting button clicked")
            if color_weakness_button.handle_event(event):
                print("Color Weakness Mode button clicked")
            if default_button.handle_event(event):
                print("Defalut button clicked")
            if back_button.handle_event(event):
                print("Default button clicked")
                running = False

        # Update buttons and title text when the window size changes
        window_size_button.update_size()
        key_setting_button.update_size()
        color_weakness_button.update_size()
        default_button.update_size()
        back_button.update_size()
        update_title_text()

        # Draw the title and buttons
        screen.blit(title_surface, title_rect)
        window_size_button.draw(screen)
        key_setting_button.draw(screen)
        color_weakness_button.draw(screen)
        default_button.draw(screen)
        back_button.draw(screen)
        pygame.display.flip()

    return True

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # Check for button clicks on the start page
        if start_button.handle_event(event):
            print("Start button clicked")
        if settings_button.handle_event(event):
            print("Settings button clicked")
            running = settings_screen()
        if exit_button.handle_event(event):
            print("Exit button clicked")
            running = False

    # Draw the title and buttons on the start page
    screen.blit(title_surface, title_rect)
    start_button.draw(screen)
    settings_button.draw(screen)
    exit_button.draw(screen)

    pygame.display.flip()

pygame.quit()


