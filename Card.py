import pygame

class Card:
    cards = {
        "Sword Slash": (pygame.image.load("Images/Cards/sword_slash.jpg"), [10, 0, 0, 1]),
        "Healing Potion": (pygame.image.load("Images/Cards/healing_potion.jpg"), [0, 15, 0, 1]),
        "Shield Block": (pygame.image.load("Images/Cards/shield_block.jpg"), [0, 0, 5, 1])
    }

    @classmethod
    def get_image(cls, name):
        if name in cls.cards:
            return cls.cards[name][0]
        return None

    @classmethod
    def get_values(cls, name):
        if name in cls.cards:
            return cls.cards[name][1]
        return None