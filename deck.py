import random
from Card import Card

class Deck:
    def __init__(self):
        self.all_cards = list(Card.cards.keys())
        self.deck = self.all_cards.copy()
        random.shuffle(self.deck)
        self.hand = []
        self.discard = []

    def draw_initial_hand(self):
        self.draw_cards(3)  # Draw 3 cards initially
        for card in self.hand:
            card.display()

    def draw_cards(self, num_cards):
        for _ in range(num_cards):
            if not self.deck:
                self.reshuffle_discard_into_deck()
            if self.deck:
                self.hand.append(self.deck.pop())

    def use_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            used_card = self.hand.pop(card_index)
            self.discard.append(used_card)
            return used_card
        return None

    def reshuffle_discard_into_deck(self):
        if self.discard:
            self.deck = self.discard[:]
            self.discard.clear()
            random.shuffle(self.deck)

    def end_turn(self):
        self.discard.extend(self.hand)
        self.hand.clear()
        self.draw_cards(3)