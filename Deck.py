import random
from Card import Card

class Deck:
    def __init__(self):
        self.all_cards = list(Card.cards.keys())
        self.deck = self.all_cards[:]
        random.shuffle(self.deck)
        self.hand = []
        self.discard = []

    def draw_card(self):
        if not self.deck:  # If the deck is empty, reshuffle the discard into the deck
            self.deck = self.discard[:]
            self.discard = []
            random.shuffle(self.deck)
        if self.deck:
            return self.deck.pop()
        return None

    def draw_initial_hand(self):
        self.hand = []
        for _ in range(3):
            card = self.draw_card()
            if card is not None:
                self.hand.append(card)

    def use_card(self, card_name):
        if card_name in self.hand:
            self.hand.remove(card_name)
            self.discard.append(card_name)
            return card_name
        return None