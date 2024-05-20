
import pygame
import sys
from GameDisplay import GameDisplay
from Protagonist import Protagonist
from Enemy import Enemy

class Main:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.display = GameDisplay(self.WIDTH, self.HEIGHT)
        self.protagonist = Protagonist(self.WIDTH, self.HEIGHT)
        self.enemy = Enemy(self.WIDTH, self.HEIGHT)

    def run(self):
        running = True
        while running:
            self.display.clear_screen()

            # Handle events
            self.display.handle_events()

            # Display information for both protagonist and enemy
            self.protagonist.display_info(10, 450, 20, 520)  # Example positions for protagonist's health bar and action points
            self.enemy.display_info(300, 10, 330, 80, 380, 19)  # Example positions for enemy's health bar, enemy image, and shield

            # Update display
            pygame.display.flip()

if __name__ == "__main__":
    game = Main()
    game.run()