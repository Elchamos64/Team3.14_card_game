import pygame

class Card:
    cards = {
        "attack_card": (pygame.image.load("Images/Cards/sword_slash.jpg"), [10, 0, 0, 1]),
        "heal_card": (pygame.image.load("Images/Cards/healing_potion.jpg"), [0, 10, 0, 1]),
        "block_card": (pygame.image.load("Images/Cards/shield_block.jpg"), [0, 0, 10, 1])
    }

    @classmethod
    def get_values(cls, card_name):
        if card_name in cls.cards:
            return cls.cards[card_name][1]
        return None

    @classmethod
    def get_image(cls, name):
        if name in cls.cards:
            return cls.cards[name][0]
        return None