import random
import time


class Uno:
    def __init__(self, num_players, first_player):
        self.draw_pile = []
        self.discard_pile = []
        self.players = []
        self.current_player = 0
        self.direction = 1

        # Create the draw pile
        self.create_draw_pile()

        # Shuffle the draw pile
        random.shuffle(self.draw_pile)

        #향후 수정예정 플레이어 2명 기준 설정
        self.CPU = 1
        if first_player == "opponent":
            self.CPU = 0

        # Create the players
        for i in range(num_players):
            self.players.append([])

        # Deal the cards
        for i in range(7):
            for player in self.players:
                card = self.draw_pile.pop()
                player.append(card)

        # Set the top card of the discard pile
        self.discard_pile.append(self.draw_pile.pop())

    def create_draw_pile(self):
        # Create the number cards
        for color in ["red", "green", "blue", "yellow"]:
            for value in range(0, 10):
                self.draw_pile.append((color, value))
                self.draw_pile.append((color, value))

        # Create the action cards
        for color in ["red", "green", "blue", "yellow"]:
            self.draw_pile.append((color, "skip"))
            self.draw_pile.append((color, "reverse"))
            self.draw_pile.append((color, "draw2"))
            self.draw_pile.append((color, "wild"))

        # Create the wild cards
        for i in range(4):
            self.draw_pile.append(("wild", "wild"))
            self.draw_pile.append(("wild", "draw4"))
            self.draw_pile.append(("wild", "draw1"))
            self.draw_pile.append(("wild", "one_more"))

    def play(self):
        while True:
            # Print the top card of the discard pile
            print("Top card: ", self.discard_pile[-1])

            # Print the current player's hand
            print("Player ", self.current_player + 1, "'s hand: ", self.players[self.current_player])

            # Get the player's move
            print("Enter card to play or 'draw' to draw a card: ")
            print("Time limit 30 seconds")
            card = 0

            if self.CPU == self.current_player:
                card = self.cpu_player_card(self.players[self.current_player])
            else:
                begin = time.time()
                while card == 0:
                    end = time.time()
                    result = end - begin
                    if result >= 30:
                        break
                    card = input()

            # Handle drawing a card
            if card == "draw":
                self.players[self.current_player].append(self.draw_pile.pop())

                # Check if the player can play the card they just drew
                if self.can_play(self.players[self.current_player]):
                    print("You draw a card you can play!")

                # Move on to the next player
                self.current_player += self.direction
                if self.current_player < 0:
                    self.current_player = len(self.players) - 1
                elif self.current_player >= len(self.players):
                    self.current_player = 0

            # Handle playing a card
            else:
                card = eval(card)
                if self.is_valid(card):
                    self.players[self.current_player].remove(card)
                    self.discard_pile.append(card)

                    # Handle action cards
                    if card[1] == "skip":
                        self.current_player += self.direction * 2
                        if self.current_player < 0:
                            self.current_player = len(self.players) - 1
                        elif self.current_player >= len(self.players):
                            self.current_player = 0
                    elif card[1] == "reverse":
                        self.direction *= -1
                    elif card[1] == "draw2":
                        player_add=self.current_player + self.direction
                        if player_add < 0:
                            player_add = len(self.players) - 1
                        elif player_add >= len(self.players):
                            player_add = 0
                        for i in range(2):
                            self.players[player_add].append(self.draw_pile.pop())

                    # Handle wild cards
                    elif card[1] == "wild":
                        if self.CPU==self.current_player:
                            color=self.cpu_player_skill()
                        else:
                            color = input("Choose a color (red, green, blue, or yellow): ")
                        card = (color, "wild")
                        self.discard_pile[-1] = card

                    elif card[1] == "draw4":
                        if self.CPU == self.current_player:
                            color = self.cpu_player_skill()
                        else:
                            color = input("Choose a color (red, green, blue, or yellow): ")
                        card = (color, "wild")
                        self.discard_pile[-1] = card
                        player_add = self.current_player + self.direction
                        if player_add < 0:
                            player_add = len(self.players) - 1
                        elif player_add >= len(self.players):
                            player_add = 0
                        for i in range(4):
                            self.players[player_add].append(self.draw_pile.pop())
                    elif card[1] == "draw1":
                        if self.CPU == self.current_player:
                            color = self.cpu_player_skill()
                        else:
                            color = input("Choose a color (red, green, blue, or yellow): ")
                        card = (color, "wild")
                        self.discard_pile[-1] = card
                        if player_add < 0:
                            player_add = len(self.players) - 1
                        elif player_add >= len(self.players):
                            player_add = 0
                        self.players[player_add].append(self.draw_pile.pop())

                    elif card[1] == "one_more":
                        if self.CPU == self.current_player:
                            color = self.cpu_player_skill()
                        else:
                            color = input("Choose a color (red, green, blue, or yellow): ")
                        card = (color, "wild")
                        self.discard_pile[-1] = card
                        self.current_player -= self.direction
                        if self.current_player < 0:
                            self.current_player = len(self.players) - 1
                        elif self.current_player >= len(self.players):
                            self.current_player = 0

                    # uno 버튼 구현
                    uno_button = self.uno_button()
                    if uno_button:
                        uno_input = 0
                        uno_begin = time.time()
                        while uno_input != 0:
                            uno_end = time.time()
                            uno_input = input()
                            if uno_input == "uno":
                                if self.CPU == self.current_player:
                                    self.players[self.current_player].append(self.draw_pile.pop())
                                break
                            elif uno_begin - uno_end >= 10:
                                if self.CPU != self.current_player:
                                    self.players[self.current_player].append(self.draw_pile.pop())
                                break

                    # Move on to the next player
                    self.current_player += self.direction
                    if self.current_player < 0:
                        self.current_player = len(self.players) - 1
                    elif self.current_player >= len(self.players):
                        self.current_player = 0

            # Check for a winner
            winner = self.winner()
            if winner:
                print("Player ", winner, "wins!")
                break


    def is_valid(self, card):
        top_card = self.discard_pile[-1]
        if card[0] == top_card[0] or card[1] == top_card[1] or card[0] == "wild" or top_card[0] == "wild":
            return True
        return False

    def cpu_player_card(self,hand):
        valid_plays = [card for card in hand if self.is_valid(card)]
        if len(valid_plays) != 0:
            return valid_plays[random.randrange(len(valid_plays))]
        return "draw"

    def cpu_player_skill(self):
        color = ["red", "green", "blue", "yellow"]
        return color[random.randrange(len(color))]

    def can_play(self, hand):
        for card in hand:
            if self.is_valid(card):
                return True
        return False


    def uno_button(self):
        for i, player in enumerate(self.players):
            if len(player) == 1:
                return i + 1
        return False

    def winner(self):
        for i, player in enumerate(self.players):
            if len(player) == 0:
                return i + 1
        return False



if __name__ == "__main__":
    player_num = input("How many players?")
    first_player = input("Who is first? you or opponent")
    Games = Uno(int(player_num), first_player)
    Games.play()
