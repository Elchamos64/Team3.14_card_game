import pygame
import random

class Card:
    cards = {
        "Sword Slash": ["Sword Slash", "Images\Cards\sword_slash.jpg", "Deal 2-3 Damage", lambda protagonist, enemy: Card.attack(protagonist, enemy, 2, 3, 1)],
        "Healing Potion": ["Healing Potion", "Images\Cards\healing_potion.jpg", "Heal 0-5 Health", lambda protagonist, _: Card.heal(protagonist, 0, 5, 1)],
        "Shield Block": ["Shield Block", "Images\Cards\shield_block.jpg", "Block 5-9 Damage", lambda protagonist, _: Card.block(protagonist, 5, 9, 1)]
    }

    @staticmethod
    def load_images():
        for key, value in Card.cards.items():
            image_path = value[1]
            Card.cards[key][1] = pygame.image.load(image_path)

    @staticmethod
    def attack(protagonist, enemy, lowNum, highNum, APcost):
        if protagonist.current_action_points >= APcost:
            damage = random.randint(lowNum, highNum)
            enemy.current_health -= damage
            if enemy.current_health < 0:
                enemy.current_health = 0
            print(f"Player attacks for {damage} damage!")
            protagonist.current_action_points -= APcost

    @staticmethod
    def heal(protagonist, lowNum, highNum, APcost):
        if protagonist.current_action_points >= APcost:
            heal_amount = random.randint(lowNum, highNum)
            protagonist.current_health = min(protagonist.max_health, protagonist.current_health + heal_amount)
            print(f"Player heals for {heal_amount} health!")
            protagonist.current_action_points -= APcost

    @staticmethod
    def block(protagonist, lowNum, highNum, APcost):
        if protagonist.current_action_points >= APcost:
            block_points = random.randint(lowNum, highNum)
            protagonist.block_points += block_points
            print(f"Player blocks, gaining {block_points} block points!")
            protagonist.current_action_points -= APcost