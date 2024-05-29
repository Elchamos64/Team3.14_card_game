import random

class Deck:
    def __init__(self, all_cards):
        self.all_cards = all_cards[:]  # Copy all cards to ensure original list is not modified
        self.deck = all_cards[:]  # Start with all cards in the deck
        random.shuffle(self.deck)  # Randomize the deck
        self.hand = []  # Hand starts empty
        self.discard = []  # Discard pile starts empty

    def draw_initial_hand(self):
        self.draw_cards(3)  # Draw 3 cards initially

    def draw_cards(self, num_cards):
        for _ in range(num_cards):
            if not self.deck:  # If the deck is empty, reshuffle from discard
                self.reshuffle_discard_into_deck()
            if self.deck:  # Check again to avoid index error
                self.hand.append(self.deck.pop())

    def use_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            used_card = self.hand.pop(card_index)
            self.discard.append(used_card)
            return used_card
        return None  # Return None if invalid index

    def discard_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            discarded_card = self.hand.pop(card_index)
            self.discard.append(discarded_card)
            return discarded_card
        return None  # Return None if invalid index

    def reshuffle_discard_into_deck(self):
        if self.discard:
            self.deck = self.discard[:]
            self.discard.clear()
            random.shuffle(self.deck)

    def end_turn(self):
        # Discard all cards in hand at the end of the turn
        self.discard.extend(self.hand)
        self.hand.clear()
        # Draw 3 new cards
        self.draw_cards(3)

    def print_status(self):
        # For debugging purposes, to see the state of the deck
        print(f"Deck: {len(self.deck)} cards")
        print(f"Hand: {len(self.hand)} cards")
        print(f"Discard: {len(self.discard)} cards")

# Assuming the Card class and some example cards are defined like this:
class Card:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

# Example usage:
if __name__ == "__main__":
    # Create some example cards
    all_cards = [Card(f"Card {i+1}") for i in range(10)]

    # Initialize the deck
    deck = Deck(all_cards)
    
    # Draw initial hand
    deck.draw_initial_hand()
    deck.print_status()  # See the state of the deck

    # Use a card from hand (example)
    deck.use_card(0)
    deck.print_status()

    # End turn, which discards current hand and draws new cards
    deck.end_turn()
    deck.print_status()