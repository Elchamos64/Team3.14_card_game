import pygame
import sys

from GameDisplay import GameDisplay
from Protagonist import Protagonist
from Enemy import Enemy
from Card import Card
from deck import Deck
from CardDictionary import cards 

from Sound import Sound

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
        self.clock = pygame.time
        sound_manager = Sound()
        sound_manager.play_music('Start')
    

    def end_turn(self):
        if self.protagonist.current_action_points < self.protagonist.max_action_points:
            self.protagonist.current_action_points = self.protagonist.max_action_points
        self.enemy.enemy_action(self.clock, self.protagonist)
        self.deck.draw_cards(3)

    def player_action(self, action):
        if action == "end_turn":
            self.end_turn()
        if self.protagonist.current_action_points > 0:
            match(action):
                case "0" | "1" | "2" | "3" | "4":
                    Deck.use_card(self.deck, int(action), self.protagonist, self.enemy)
            # If action is end_turn, reset action points



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
        self.deck.draw_initial_hand()
        self.deck.draw_initial_hand()
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

            
            # Draw card areas
            self.display.draw_card_areas(self.deck)

            # Draw buttons
            self.display.draw_button_areas()

            # Update display
            pygame.display.flip()



if __name__ == "__main__":
    game = Main()
    game.run()