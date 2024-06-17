import pygame
import sys
import random
from GameDisplay import GameDisplay
from Protagonist import Protagonist
from Enemy import Enemy
from Card import Card
from deck import Deck
from CardDictionary import cards 

class Main:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.display = GameDisplay(self.WIDTH, self.HEIGHT)
        self.protagonist = Protagonist(self.WIDTH, self.HEIGHT)
        self.enemy = Enemy(self.WIDTH, self.HEIGHT)
        self.deck = Deck(cards)
        self.actions = ["attack", "heal", "block"]
        self.card = Card

    def end_turn(self):
        if self.protagonist.current_action_points < self.protagonist.max_action_points:
            self.protagonist.current_action_points = self.protagonist.max_action_points
        self.enemy_action()

    def player_action(self, action):
        if self.protagonist.current_action_points > 0:
            match(action):
                case "0" | "1" | "2" | "3" | "4":
                    Deck
                    Deck.use_card(self.deck, int(action), self.protagonist, self.enemy)
            # If action is end_turn, reset action points
                case "end_turn":
                    self.end_turn()

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

            # Check for game over
            if self.check_game_over():
                running = False

            # Display information for both protagonist and enemy
            self.protagonist.display_info(40, 450, 20, 520, 70, 515)  # Updated positions for protagonist's health bar, action points, and shield
            self.enemy.display_info(300, 10, 330, 80, 380, 18)  # Updated positions for enemy's health bar, enemy image, and shield

            self.deck.draw_initial_hand()
            # Draw card areas
            self.display.draw_card_areas(self.deck)

            # Draw buttons
            self.display.draw_button_areas()

            # Update display
            pygame.display.flip()



if __name__ == "__main__":
    game = Main()
    game.run()