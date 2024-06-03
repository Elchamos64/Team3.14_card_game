import pygame
import sys
from Protagonist import Protagonist
import random
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

    def attack(self, lowNum, highNum, APcost):
        lowNum = 5
        highNum = 15
        damage = random.randint(lowNum, highNum)
        self.enemy.current_health -= damage
        if self.enemy.current_health < 0:
            self.enemy.current_health = 0
        print(f"Player attacks for {damage} damage!")
        
        # Reduce action points after performing an action
        self.protagonist.reduce_action_points()

    def heal(self,lowNum, highNum, APcost):
        heal_amount = random.randint(10, 20)
        self.protagonist.current_health = min(self.protagonist.max_health, self.protagonist.current_health + heal_amount)
        print(f"Player heals for {heal_amount} health!")

        # Reduce action points after performing an action
        self.protagonist.reduce_action_points()

    def block(self, lowNum, highNum, APcost):
        block_points = random.randint(5, 10)
        self.protagonist.block_points += block_points
        print(f"Player blocks, gaining {block_points} block points!")

        # Reduce action points after performing an action
        self.protagonist.reduce_action_points()
