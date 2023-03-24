import pygame
from Game import Uno

class Deck_card(pygame.sprite.Sprite):
    def __init__(self, color, value, index):
        super().__init__()
        # set wild cards' color as black
        if color == "wild":
            color = 'black'

        # action & wild cards
        if value in {"skip", "reverse", "draw2", "wild", "draw4", "draw1", "one_more"}:
            # TODO: place logo on card
            pass
        # number cards
        else:
            # TODO: place number on card
            pass

        x_pos = index * 80
        y_pos = 450

        self.image = pygame.image.load('graphics/'+color+'.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (59, 91)) # /12
        self.rect = self.image.get_rect(topleft = (x_pos, y_pos))

    def clicked(self):
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                print("Left Mouse key was clicked")
                pass

    def update(self):
        self.clicked()


# TODO: get time from game.py
def display_timer():
    timer_surf = font.render('timer', False, 'Black')
    timer_rect = timer_surf.get_rect(topright = (800, 0))
    pygame.draw.rect(screen, 'Pink', timer_rect)
    screen.blit(timer_surf, timer_rect)
    

pygame.init()

# Main window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('UNO Game')
clock = pygame.time.Clock()

# Groups
card_group = pygame.sprite.Group()

# Load draw pile
card_surf = pygame.image.load('graphics/black.png').convert_alpha()
card_surf = pygame.transform.scale(card_surf, (59, 91)) # /12
card_rect = card_surf.get_rect(midbottom = (200,300))

# Timer
font = pygame.font.Font(None, 50)


# Create the highlight surface
highlight_surf = pygame.Surface(card_surf.get_size(), pygame.SRCALPHA)
highlight_surf.fill((255, 255, 0, 50))

# Game state: start_menu, playing, game_over, pause
state = 'playing'

# set game over text
game_over_text = font.render("Press anykey!", True, 'White')

# set start menu text
start_menu_text = font.render("Press any key to start", True, 'White')

# single game
game = Uno(1, 0)
deck = game.players[game.current_player]

# Create instances of the Deck_card class for each card in the deck
#for i, card in enumerate(game.players[0]): # Player 0's deck
for i, card in enumerate([('red', 7), ('red', 4), ('green', 4), ('red', 6), ('red', 6), ('red', 4), ('yellow', 6)]):
    color, number = card
    card_sprite = Deck_card(color, int(number), i)
    card_group.add(card_sprite)



# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Close button event
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # if game over, go back to start menu when any key is pressed
            if state == "game_over":
                state = "start_menu"



    # Game playing screen
    if state == 'playing':

        screen.fill('white')
        display_timer()

        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        card_group.draw(screen)
        card_group.update()



        # Check if the mouse is hovering over the card
        if card_rect.collidepoint(mouse_pos):
            # Draw the card surface and the highlight surface
            screen.blit(card_surf,card_rect)
            screen.blit(highlight_surf, card_rect)

            # Check if the left mouse button is clicked
            if pygame.mouse.get_pressed()[0]:
                print("Left Mouse key was clicked")
                #state = 'game_over'

        else:
            # Draw only the card surface
            screen.blit(card_surf,card_rect)



    # Game over menu
    elif state == 'game_over':
        screen.fill('Black')
        screen.blit(game_over_text, (400 - game_over_text.get_width()/2, 300 - game_over_text.get_height()/2))        

    # Start menu
    elif state == 'start_menu':
        pass


    # Update the screen
    pygame.display.update()

    # Limit the frame rate to 60 frames per second
    clock.tick(30)

# Quit pygame
pygame.quit()