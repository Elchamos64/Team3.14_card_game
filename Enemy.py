import pygame
import sys
from GameDisplay import GameDisplay
import random
from Protagonist import Protagonist

class Enemy(GameDisplay):
    def __init__(self, width, height):
        super().__init__(width, height)
        # Additional attributes for Enemy
        self.max_health = 50
        self.current_health = 50
        self.block_points = 25  # Example block points

        # Load enemy image and scale it
        self.enemy_image = pygame.image.load("Images/Enemies/MilkJugSteve.png")  # Replace with your actual enemy image file
        self.enemy_image = pygame.transform.scale(self.enemy_image, (self.enemy_image.get_width() * 3, self.enemy_image.get_height() * 3))  # Adjust the size as needed

    def display_info(self, health_bar_x, health_bar_y, enemy_x, enemy_y, shield_x, shield_y):
        # Draw health bar
        health_bar_width = 200
        health_bar_height = 20
        super().draw_health_bar(self.current_health, self.max_health, health_bar_x, health_bar_y, health_bar_width, health_bar_height)

        # Render health text
        health_text = self.font.render(f"{self.current_health}/{self.max_health}", True, (0, 0, 0))  # Black color
        health_text_x = health_bar_x + (health_bar_width - health_text.get_width()) // 8  # Center the text horizontally within the health bar
        health_text_y = health_bar_y + (health_bar_height - health_text.get_height()) * 4  # Center the text vertically within the health bar

        # Blit health text
        self.screen.blit(health_text, (health_text_x, health_text_y))

        # Draw the enemy image
        self.screen.blit(self.enemy_image, (enemy_x, enemy_y))

        # Draw the shield and block points
        self.draw_shield_and_block_points(shield_x, shield_y, self.block_points)
    
    def enemy_action(self):
        #Move to another class, add multiple actions and bigger actions based on amount of turns
        action = random.choice(self.actions)
        if action == "attack":
            damage = random.randint(5, 15)
            self.protagonist.block_points -= damage
            if self.protagonist.block_points < 0:
                self.protagonist.current_health += self.protagonist.block_points
                self.protagonist.block_points = 0
                if self.protagonist.current_health < 0:
                    self.protagonist.current_health = 0
            print(f"Enemy attacks for {damage} damage!")
        elif action == "heal":
            heal_amount = random.randint(5, 10)
            self.enemy.current_health = min(self.enemy.max_health, self.enemy.current_health + heal_amount)
            print(f"Enemy heals for {heal_amount} health!")
        elif action == "block":
            block_points = random.randint(5, 10)
            self.enemy.block_points += block_points
            print(f"Enemy blocks, gaining {block_points} block points!")