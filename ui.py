import pygame
from game import Uno

class Card(pygame.sprite.Sprite):
    def __init__(self, color, value):
        super().__init__()

        # Set wild card's color as black
        if color == "wild":
            color = 'black'

        self.image = pygame.image.load('graphics/' + color + '.png').convert_alpha()
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

        # get the center position of the card image
        center_x = self.image.get_width() // 2
        center_y = self.image.get_height() // 2
        # get the center position of the text surface
        text_x = center_x - text_surf.get_width() // 2
        text_y = center_y - text_surf.get_height() // 2
        # blit the text surface onto the card image
        #text_rect = text_surf.get_rect(center=self.rect.center)
        self.image.blit(text_surf, (text_x, text_y))

class HandCard(Card):
    def __init__(self, color, value, index):
        super().__init__(color, value)
        self.rect.topleft = (index * 75 + 20, 450)

    def clicked(self):
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                print("Left Mouse key was clicked")

    def update(self):
        self.clicked()

class DrawPile(Card):
    def __init__(self):
        super().__init__('back', '')
        self.rect.midbottom = (200, 300)

    def clicked(self):
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                print("Left Mouse key was clicked")

    def update(self):
        self.clicked()

class DiscardPile(Card):
    def __init__(self, pile):
        color, value = pile[-1]
        super().__init__(color, value)
        self.rect.midbottom = (300, 300)

    def update(self):
        pass

class PlayerHand(pygame.sprite.Sprite):
    def __init__(self, player_number, number_of_cards):
        super().__init__()
        self.image = pygame.Surface((250, 150))
        self.image.fill('white')
        self.rect = self.image.get_rect(topright=(800, player_number * 100))
        self.card_group = pygame.sprite.Group()
        
        # add card sprites to the sprite group
        card_width = 35
        card_height = 55
        card_spacing = 20
        for i in range(number_of_cards):
            card = Card('back', '')
            card.image = pygame.transform.scale(card.image, (card_width, card_height))
            card.rect.x = 10 + i * card_spacing
            card.rect.y = 80
            self.card_group.add(card)
        
        # update the player hand sprite image with the card sprites
        self.card_group.draw(self.image)

    def update(self):
        pass


def timer():
    # TODO: get time from Uno class
    timer_surf = font.render('timer', False, 'black')
    timer_rect = timer_surf.get_rect(topleft = (0, 0))
    pygame.draw.rect(screen, 'Pink', timer_rect)
    screen.blit(timer_surf, timer_rect)
    
def uno_button():
    # set up button properties
    font = pygame.font.Font(None, 40)
    text = font.render("Uno", True, 'black')

    # create button surface
    button_surf = pygame.Surface((100, 50))
    button_surf.fill('white')
    button_rect = button_surf.get_rect(midbottom = (450, 300))

    # blit text onto button surface
    text_rect = text.get_rect(center=button_surf.get_rect().center)
    button_surf.blit(text, text_rect)

    screen.blit(button_surf, button_rect)

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            print("Left Mouse key was clicked")

def current_color():
    color_dict = {
    'green': '#00AC67',
    'red': '#F35959',
    'blue': '#006CB4',
    'yellow': '#EED324'
}
    # TODO: get color from Uno class, not from pile
    color, _ = game.discard_pile[-1]
    if color == 'wild': color = 'black'

    # Create a color surface
    color_surf = pygame.Surface((50, 50))
    color_surf.fill(color_dict[color])
    color_rect = color_surf.get_rect(midbottom = (450, 240))

    # Blit the color surface onto the game screen
    screen.blit(color_surf, color_rect)

pygame.init()

# Main window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('UNO Game')
clock = pygame.time.Clock()

# Single game
game = Uno(2, 0)
my_hand = game.players[0]
others_hand = game.players[1:]

# Sprites
hand_card = pygame.sprite.Group()
for i, card in enumerate(my_hand):
    color, value = card
    card_sprite = HandCard(color, value, i)
    hand_card.add(card_sprite)

draw_pile = pygame.sprite.GroupSingle()
draw_pile.add(DrawPile())

discard_pile = pygame.sprite.GroupSingle()
discard_pile.add(DiscardPile(game.discard_pile))

player_list = pygame.sprite.Group()
for i, player in enumerate(others_hand):
    player_number = i
    number_of_cards = len(player)
    hand_sprite = PlayerHand(player_number, number_of_cards)
    player_list.add(hand_sprite)


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
        screen.fill('lavender')



        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        timer()
        uno_button()
        current_color()

        # my deck
        hand_card.draw(screen)
        hand_card.update()

        # draw pile
        draw_pile.draw(screen)
        draw_pile.update()

        # discard pile
        discard_pile.draw(screen)
        discard_pile.update()

        # player list
        player_list.draw(screen)
        player_list.update()



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