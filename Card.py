import pygame
import sys
from Protagonist import Protagonist
from Enemy import Enemy
import random
class Card:
    def __init__(self, iName, iPicture, iText, iRun):
        super().__init__()
        pygame.font.init()
        #define card 
        self.name = iName
        self.picture = pygame.image.load(iPicture)
        self.text = iText
        self.run = iRun
        self.cardfront = pygame.image.load("Images\Display\CardFront.png")
        self.cardfront = pygame.transform.scale(self.cardfront, (65, 85))
        self.font = pygame.font.SysFont(None, 12)
        self.nameFont = pygame.font.SysFont(None, 20)
        self.enemy = Enemy
        self.protagonist = Protagonist

        def run():
            pass
        
        # #define cards and replace with images
        # self.kick = pygame.image.load()
        # self.hands_up = pygame.image.load()
        # self.deep_breath = pygame.image.load()

        # #scale images
        # self.kick = pygame.transform.scale(self.kick, (100, 150))
        # self.hands_up = pygame.transform.scale(self.hands_up, (100, 150))
        # self.deep_breath = pygame.transform.scale(self.deep_breath, (100, 150))

    def attack(self, lowNum, highNum, APcost):
        if self.protagonist.current_action_points > 0:
            damage = random.randint(lowNum, highNum)
            self.enemy.current_health -= damage
            if self.enemy.current_health < 0:
                self.enemy.current_health = 0
            print(f"Player attacks for {damage} damage!")
            # Reduce action points after performing an action
            self.protagonist.reduce_action_points(APcost)

    def heal(self,lowNum, highNum, APcost):
        if self.protagonist.current_action_points > 0:
            heal_amount = random.randint(lowNum, highNum)
            self.protagonist.current_health = min(self.protagonist.max_health, self.protagonist.current_health + heal_amount)
            print(f"Player heals for {heal_amount} health!")
            # Reduce action points after performing an action
            self.protagonist.reduce_action_points(APcost)

    def block(self, lowNum, highNum, APcost):
        if self.protagonist.current_action_points > 0:
            block_points = random.randint(lowNum, highNum)
            self.protagonist.block_points += block_points
            print(f"Player blocks, gaining {block_points} block points!")
            # Reduce action points after performing an action
            self.protagonist.reduce_action_points(APcost)

    def display(self, screen, x, y):
        screen.blit(self.cardfront, (x, y, 100, 130))   
        box_points_text = self.font.render(str(self.text), True, (0, 0, 0))  # Black color
        screen.blit(box_points_text, (x, y+75))
        box_points_name = self.nameFont.render(str(self.name), True, (0, 0, 0))  # Black color
        screen.blit(box_points_name, (x, y+5))
        