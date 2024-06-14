import pygame
import Random

class Card:
    cards = {
        "Sword Slash": (pygame.image.load("Images/Cards/sword_slash.jpg"), [10, 0, 0, 1]),
        "Healing Potion": (pygame.image.load("Images/Cards/healing_potion.jpg"), [0, 15, 0, 1]),
        "Shield Block": (pygame.image.load("Images/Cards/shield_block.jpg"), [0, 0, 5, 1])
    }

    def attack(self, lowNum, highNum, APcost):
        if self.protagonist.current_action_points > 0:
            damage = Random.randint(lowNum, highNum)
            self.enemy.current_health -= damage
            if self.enemy.current_health < 0:
                self.enemy.current_health = 0
            print(f"Player attacks for {damage} damage!")
            # Reduce action points after performing an action
            self.protagonist.reduce_action_points(APcost)

    def heal(self,lowNum, highNum, APcost):
        if self.protagonist.current_action_points > 0:
            heal_amount = Random.randint(lowNum, highNum)
            self.protagonist.current_health = min(self.protagonist.max_health, self.protagonist.current_health + heal_amount)
            print(f"Player heals for {heal_amount} health!")
            # Reduce action points after performing an action
            self.protagonist.reduce_action_points(APcost)

    def block(self, lowNum, highNum, APcost):
        if self.protagonist.current_action_points > 0:
            block_points = Random.randint(lowNum, highNum)
            self.protagonist.block_points += block_points
            print(f"Player blocks, gaining {block_points} block points!")
            # Reduce action points after performing an action
            self.protagonist.reduce_action_points(APcost)

    def display(self, screen, x, y):
        screen.blit(self.cardfront, (x, y, 100, 130))   
        box_points_text = self.font.render(str(self.text), True, (0, 0, 0))  # Black color
        screen.blit(self.picture, (x+5, y+20, 50, 50))
        screen.blit(box_points_text, (x, y+75))
        box_points_name = self.nameFont.render(str(self.name), True, (0, 0, 0))  # Black color
        screen.blit(box_points_name, (x, y+5))