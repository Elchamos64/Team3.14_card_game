import pygame
import sys

class Card:
    def __init__(self):
        super().__init__()
        
        #define cards and replace with images
        self.kick = pygame.image.load()
        self.hands_up = pygame.image.load()
        self.deep_breath = pygame.image.load()

        #scale images
        self.kick = pygame.transform.scale(self.kick, (100, 150))
        self.hands_up = pygame.transform.scale(self.hands_up, (100, 150))
        self.deep_breath = pygame.transform.scale(self.deep_breath, (100, 150))

    def attack(lowNum, highNum, APcost):
        #TODO implement attack function
        pass

    def heal(lowNum, highNum, APcost):
        #TODO implement heal function
        pass

    def block(lowNum, highNum, APcost):
        #TODO implement block function
        pass

