import random
from Card import Card

class Deck:
    def __init__(self, cards):
        self.fighter = [
            cards["Shield Block"],
            cards["Shield Block"], 
            cards["Sword Slash"],
            cards["Sword Slash"],
            cards["Heal Potion"],
            cards["Kick"],
            cards["Kick"],
            cards["Investigate"],
        ]

        self.wizard = [
            cards["Fireball"],
            cards["Heal Potion"],
            cards["Heal Potion"],
            cards["Kick"],
            cards["Kick"],
            cards["Eureka!"],
            cards["Eureka!"],
            cards["Hide"],
        ]

        self.ninja = [
            cards["Shruiken"],
            cards["Shruiken"],
            cards["Shruiken"],
            cards["Hide"],
            cards["Hide"],
            cards["Near Miss"],
            cards["Investigate"],
            cards["Investigate"],
        ]

        self.deck = self.wizard
        random.shuffle(self.deck)
        self.hand = []
        self.discard = []
    
    def initialize_deck1(self):
        self.deck=[]
        self.deck = self.fighter
    
    def initialize_deck2(self):
        self.deck=[]
        self.deck = self.wizard
    
    def initialize_deck3(self):
        self.deck=[]
        self.deck = self.ninja

    def draw_initial_hand(self):
        self.draw_cards(3)  # Draw 3 cards initially

    #Brings cards from the deck array to the hand array
    def draw_cards(self, num_cards):
        for _ in range(num_cards):
            if not self.deck:
                self.reshuffle_discard_into_deck()
            if (self.deck) and (len(self.hand) < 5):
                self.hand.append(self.deck.pop())

    #Brings cards from the hand array to the discard array
    def use_card(self, card_index, protagonist, enemy):
        if 0 <= card_index < len(self.hand):
            used_card = self.hand.pop(card_index)
            if used_card.run[3] <= protagonist.current_action_points:
                used_card.runCard(protagonist, enemy, self)
                self.discard.append(used_card)
            else:
                self.hand.append(used_card)
            return used_card
        return None

    #Brings cards from the discard array to the deck array and randomizes the deck array
    def reshuffle_discard_into_deck(self):
        if self.discard:
            self.deck = self.discard[:]
            self.discard.clear()
            random.shuffle(self.deck)

    #Give the size of the cards for display and integration.
    def draw_card_areas(self, screen):
        x = 150
        y = 480
        for card in self.hand:
            card.display(screen, x, y)
            x += 70

    #Change the deck according to the chosen hero
    def choose_deck(self, choice):
        if choice == 'fighter':
            self.initialize_deck1()
        elif choice == 'wizard':
            self.initialize_deck2()
        elif choice == 'ninja':
            self.initialize_deck3()
        else:
            print("Invalid choice. No changes made.")