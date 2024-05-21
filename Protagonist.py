import pygame
import sys
from GameDisplay import GameDisplay

class Protagonist(GameDisplay):
    def __init__(self, width, height):
        super().__init__(width, height)
        # Additional attributes for Protagonist
        self.max_health = 100
        self.current_health = 50
        self.current_action_points = 10
        self.max_action_points = 10

        # Load action point image and scale it
        self.action_point_image = pygame.image.load("Images/Display/ActionPoints.png")
        self.action_point_image = pygame.transform.scale(self.action_point_image, (self.action_point_image.get_width() * 4, self.action_point_image.get_height() * 4))  # Adjust the size as needed

    def display_info(self, health_bar_x, health_bar_y, action_point_x, action_point_y):
        # Draw health bar
        health_bar_width = 200
        health_bar_height = 20
        super().draw_health_bar(self.current_health, self.max_health, health_bar_x, health_bar_y, health_bar_width, health_bar_height)

        # Render health text
        health_text = self.font.render(f"{self.current_health}/{self.max_health}", True, (0, 0, 0))  # Black color
        health_text_x = health_bar_x + (health_bar_width - health_text.get_width()) // 9 # Center the text horizontally within the health bar
        health_text_y = health_bar_y + (health_bar_height - health_text.get_height()) * 4 # Center the text vertically within the health bar

        # Blit health text
        self.screen.blit(health_text, (health_text_x, health_text_y))

        # Draw action points
        self.draw_action_points(action_point_x, action_point_y)

    def draw_action_points(self, action_point_x, action_point_y):
        # Draw the action point image
        self.screen.blit(self.action_point_image, (action_point_x, action_point_y))

        # Render action point text
        action_point_text = self.font.render(str(self.current_action_points), True, (0, 0, 0))  # Black color
        text_rect = action_point_text.get_rect(center=(action_point_x + self.action_point_image.get_width() // 2, action_point_y + self.action_point_image.get_height() // 2))

        # Blit action point text
        self.screen.blit(action_point_text, text_rect)