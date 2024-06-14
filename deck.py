import random
from Card import Card

class Deck:
    def __init__(self, cards):
        self.all_cards = list(cards.values())
        self.deck = self.all_cards.copy()
        random.shuffle(self.deck)
        self.hand = []
        self.discard = []

    def draw_initial_hand(self):
        self.draw_cards(3)  # Draw 3 cards initially

    #Brings cards from the deck array to the hand array
    def draw_cards(self, num_cards):
        for _ in range(num_cards):
            if not self.deck:
                self.reshuffle_discard_into_deck()
            if self.deck:
                self.hand.append(self.deck.pop())

    #Brings cards from the hand array to the discard array
    def use_card(self, card_index, protagonist, enemy):
        if 0 <= card_index < len(self.hand):
            used_card = self.hand.pop(card_index)
            used_card.runCard(protagonist, enemy)
            self.discard.append(used_card)
            return used_card
        return None

    #Brings cards from the discard array to the deck array and randomizes the deck array
    def reshuffle_discard_into_deck(self):
        if self.discard:
            self.deck = self.discard[:]
            self.discard.clear()
            random.shuffle(self.deck)

    #Starts process for hand array to gain three cards from the deck array.
    def end_turn(self):
        self.discard.extend(self.hand)
        self.hand.clear()
        self.draw_cards(3)
    
    #Give the size of the cards for display and integration.
    def draw_card_areas(self, screen):
        x = 150
        y = 480
        for card in self.hand:
            card.display(screen, x, y)
            x += 70