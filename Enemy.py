import pygame
import sys
from GameDisplay import GameDisplay

class Enemy(GameDisplay):
    def __init__(self, width, height):
        super().__init__(width, height)
        # Additional attributes for Enemy
        self.max_health = 50
        self.current_health = 20
        self.block_points = 25  # Example block points

        # Load enemy image and scale it
        self.enemy_image = pygame.image.load("Images/Enemies/MilkJugSteve.png")  # Replace with your actual enemy image file
        self.enemy_image = pygame.transform.scale(self.enemy_image, (self.enemy_image.get_width() * 3, self.enemy_image.get_height() * 3))  # Adjust the size as needed

        # Load shield image and scale it
        self.shield_image = pygame.image.load("Images/Enemies/Shield.png")  # Replace with your actual shield image file
        self.shield_image = pygame.transform.scale(self.shield_image, (self.shield_image.get_width() * 4, self.shield_image.get_height() * 4))  # Adjust the size as needed

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
        self.draw_shield_and_block_points(shield_x, shield_y)

    def draw_shield_and_block_points(self, shield_x, shield_y):
        # Draw the shield image
        self.screen.blit(self.shield_image, (shield_x, shield_y))

        # Render block points text
        block_points_text = self.font.render(str(self.block_points), True, (0, 0, 0))  # Black color
        text_rect = block_points_text.get_rect(center=(shield_x + self.shield_image.get_width() // 2, shield_y + self.shield_image.get_height() // 2))

        # Blit block points text
        self.screen.blit(block_points_text, text_rect)