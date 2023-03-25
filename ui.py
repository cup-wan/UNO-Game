import pygame
from game import Uno

class Card(pygame.sprite.Sprite):
    def __init__(self, color, value):
        super().__init__()

        # Set wild card's color as black
        if color == "wild":
            color = 'black'

        self.image = pygame.image.load('graphics/' + color + '.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (59, 91)) # /12
        self.rect = self.image.get_rect()

        font = pygame.font.Font(None, 40)
        # action & wild cards
        symbols = {
            "skip": "S",
            "reverse": "R",
            "draw2": "+2",
            "wild": "W",
            "draw4": "+4",
            "draw1": "+1",
            "one_more": "1+"
        }
        if value in symbols:
            symbol = symbols[value]
            text_surf = font.render(symbol, True, 'black')

        # number cards
        else:
            text_surf = font.render(str(value), True, 'black')

        # TODO: Use rect
        # get the center position of the card image
        center_x = self.image.get_width() // 2
        center_y = self.image.get_height() // 2
        # get the center position of the text surface
        text_x = center_x - text_surf.get_width() // 2
        text_y = center_y - text_surf.get_height() // 2
        # blit the text surface onto the card image
        #text_rect = text_surf.get_rect(center=self.rect.center)
        self.image.blit(text_surf, (text_x, text_y))

class Deck_card(Card):
    def __init__(self, color, value, index):
        super().__init__(color, value)

        self.rect.topleft = (index * 75 + 20, 450)

    def clicked(self):
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                print("Left Mouse key was clicked")

    def update(self):
        self.clicked()

class Draw_pile(Card):
    def __init__(self):
        super().__init__('black', '')
        self.rect.midbottom = (200, 300)

    def clicked(self):
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                print("Left Mouse key was clicked")

    def update(self):
        self.clicked()

class Discard_pile(Card):
    def __init__(self, pile):
        color, value = pile[-1]
        super().__init__(color, value)
        self.rect.midbottom = (300, 300)

    def update(self):
        pass


class Player_list(pygame.sprite.Sprite):
    def __init__(self, color, value, index):
        super().__init__()
        550

# TODO: get time from Uno class
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

# Single game
game = Uno(1, 0)
deck = game.players[game.current_player]

# Sprites
deck_cards = pygame.sprite.Group()
for i, card in enumerate(deck):
    color, value = card
    card_sprite = Deck_card(color, value, i)
    deck_cards.add(card_sprite)

draw_pile = pygame.sprite.GroupSingle()
draw_pile.add(Draw_pile())

discard_pile = pygame.sprite.GroupSingle()
discard_pile.add(Discard_pile(game.discard_pile))


# font
font = pygame.font.Font(None, 50)


# # Create the highlight surface
# highlight_surf = pygame.Surface(draw_surf.get_size(), pygame.SRCALPHA)
# highlight_surf.fill((255, 255, 0, 50))

# Game state: start_menu, playing, game_over, pause
state = 'playing'

# TODO: show winner
game_over_text = font.render("Press anykey!", True, 'White')

# TODO: show proper start menu
start_menu_text = font.render("Press any key to start", True, 'White')







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

        # my deck
        deck_cards.draw(screen)
        deck_cards.update()

        # draw pile
        draw_pile.draw(screen)
        draw_pile.update()

        # discard pile
        discard_pile.draw(screen)
        discard_pile.update()

        # player list




        # # Check if the mouse is hovering over the card
        # if draw_rect.collidepoint(mouse_pos):
        #     # Draw the card surface and the highlight surface
        #     screen.blit(draw_surf,draw_rect)
        #     screen.blit(highlight_surf, draw_rect)

        #     # Check if the left mouse button is clicked
        #     if pygame.mouse.get_pressed()[0]:
        #         print("Left Mouse key was clicked")
        #         #state = 'game_over'

        # else:
        #     # Draw only the card surface
        #     screen.blit(draw_surf,draw_rect)



    # TODO: game over screen
    elif state == 'game_over':
        screen.fill('Black')
        screen.blit(game_over_text, (400 - game_over_text.get_width()/2, 300 - game_over_text.get_height()/2))        

    # TODO: Start menu
    elif state == 'start_menu':
        pass


    # Update the screen
    pygame.display.update()

    # Limit the frame rate to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()