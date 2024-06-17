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
        if isinstance(iPicture, str):
            self.picture = pygame.image.load(iPicture)
        else:
            self.picture = iPicture
        self.picture = pygame.transform.scale(self.picture, (50, 50))
        self.text = iText
        self.run = iRun
        self.cardfront = pygame.image.load("Images\Display\CardFront.png")
        self.cardfront = pygame.transform.scale(self.cardfront, (65, 85))
        self.font = pygame.font.SysFont(None, 12)
        self.nameFont = pygame.font.SysFont(None, 20)




            
    def runCard(self, protagonist, enemy):
        if self.run[0] == 'attack':
            self.attack(self.run[1], self.run[2], self.run[3], protagonist, enemy)
        if self.run[0] == 'heal':
            self.heal(self.run[1], self.run[2], self.run[3], protagonist)            
        if self.run[0] == 'block':
            self.block(self.run[1], self.run[2], self.run[3], protagonist)

    def attack(self, lowNum, highNum, APcost, protagonist, enemy):
        if protagonist.current_action_points > APcost:
            damage = random.randint(lowNum, highNum)
            enemy.block_points -= damage
            if enemy.block_points < 0:
                enemy.current_health += enemy.block_points
                enemy.block_point = 0
                if enemy.current_health < 0:
                    enemy.current_health = 0
            print(f"Player attacks for {damage} damage!")
            # Reduce action points after performing an action
            protagonist.reduce_action_points(APcost)

    def heal(self,lowNum, highNum, APcost, protagonist):
        if protagonist.current_action_points > APcost:
            heal_amount = random.randint(lowNum, highNum)
            protagonist.current_health = min(protagonist.max_health, protagonist.current_health + heal_amount)
            print(f"Player heals for {heal_amount} health!")
            # Reduce action points after performing an action
            protagonist.reduce_action_points(APcost)

    def block(self, lowNum, highNum, APcost, protagonist):
        if protagonist.current_action_points > APcost:
            block_points = random.randint(lowNum, highNum)
            protagonist.block_points += block_points
            print(f"Player blocks, gaining {block_points} block points!")
            # Reduce action points after performing an action
            protagonist.reduce_action_points(APcost)

    def display(self, screen, x, y):
        screen.blit(self.cardfront, (x, y, 100, 130))   
        box_points_text = self.font.render(str(self.text), True, (0, 0, 0))  # Black color
        screen.blit(self.picture, (x+5, y+20, 50, 50))
        screen.blit(box_points_text, (x, y+75))
        box_points_name = self.nameFont.render(str(self.name), True, (0, 0, 0))  # Black color
        screen.blit(box_points_name, (x, y+5))
        