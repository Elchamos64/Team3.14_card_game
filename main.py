import pygame
import sys
import random
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
        self.actions = ["attack", "heal", "block"]

    def player_action(self, action):
        if action == "attack":
            damage = random.randint(5, 15)
            self.enemy.current_health -= damage
            print(f"Player attacks for {damage} damage!")
        elif action == "heal":
            heal_amount = random.randint(10, 20)
            self.protagonist.current_health = min(self.protagonist.max_health, self.protagonist.current_health + heal_amount)
            print(f"Player heals for {heal_amount} health!")
        elif action == "block":
            block_points = random.randint(5, 10)
            self.protagonist.action_points += block_points
            print(f"Player blocks, gaining {block_points} action points!")
    
    def enemy_action(self):
        action = random.choice(self.actions)
        if action == "attack":
            damage = random.randint(5, 15)
            self.protagonist.current_health -= damage
            print(f"Enemy attacks for {damage} damage!")
        elif action == "heal":
            heal_amount = random.randint(5, 10)
            self.enemy.current_health = min(self.enemy.max_health, self.enemy.current_health + heal_amount)
            print(f"Enemy heals for {heal_amount} health!")
        elif action == "block":
            block_points = random.randint(5, 10)
            self.enemy.block_points += block_points
            print(f"Enemy blocks, gaining {block_points} block points!")

    def check_game_over(self):
        if self.protagonist.current_health <= 0:
            print("Game Over! Enemy wins!")
            return True
        elif self.enemy.current_health <= 0:
            print("Game Over! Player wins!")
            return True
        return False

    def run(self):
        running = True
        while running:
            self.display.clear_screen()

            # Handle events
            action = self.display.handle_events()
            if action:  # If an action was returned
                self.player_action(action)
                self.enemy_action()  # Enemy's turn

            # Check for game over
            if self.check_game_over():
                running = False

            # Display information for both protagonist and enemy
            self.protagonist.display_info(10, 450, 20, 520)  # Example positions for protagonist's health bar and action points
            self.enemy.display_info(300, 10, 330, 80, 380, 19)  # Example positions for enemy's health bar, enemy image, and shield

            # Draw card areas
            self.display.draw_card_areas()

            # Update display
            pygame.display.flip()


if __name__ == "__main__":
    game = Main()
    game.run()