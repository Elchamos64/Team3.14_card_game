import pygame
import sys
import random
from GameDisplay import GameDisplay
from Protagonist import Protagonist
from Enemy import Enemy
from Card import Card
from Deck import Deck

class Main:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.display = GameDisplay(self.WIDTH, self.HEIGHT)
        self.protagonist = Protagonist(self.WIDTH, self.HEIGHT)
        self.enemy = Enemy(self.WIDTH, self.HEIGHT)
        self.actions = ["attack", "heal", "block"]
        self.deck = Deck()
        self.deck.draw_initial_hand()

    def end_turn(self):
        self.protagonist.current_action_points = self.protagonist.max_action_points
        self.enemy_action()
        self.deck.deck.extend(self.deck.discard)
        self.deck.discard.clear()
        self.deck.draw_initial_hand()

    def player_action(self, card_name):
        if card_name:
            card_values = Card.get_values(card_name)
            if card_values:
                attack_damage, heal_amount, block_points, ap_cost = card_values
                if self.protagonist.current_action_points >= ap_cost:
                    self.protagonist.current_action_points -= ap_cost
                    used_card = self.deck.use_card(card_name)
                    if used_card:
                        print(f"Used card: {used_card}")
                        if attack_damage > 0:
                            self.enemy.current_health -= attack_damage
                            if self.enemy.current_health < 0:
                                self.enemy.current_health = 0
                        if heal_amount > 0:
                            self.protagonist.current_health = min(self.protagonist.max_health, self.protagonist.current_health + heal_amount)
                        if block_points > 0:
                            self.protagonist.block_points += block_points

    def enemy_action(self):
        action = random.choice(self.actions)
        if action == "attack":
            damage = random.randint(5, 15)
            self.protagonist.current_health -= damage
            if self.protagonist.current_health < 0:
                self.protagonist.current_health = 0
        elif action == "heal":
            heal_amount = random.randint(5, 10)
            self.enemy.current_health = min(self.enemy.max_health, self.enemy.current_health + heal_amount)
        elif action == "block":
            block_points = random.randint(5, 10)
            self.enemy.block_points += block_points

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
            action = self.display.handle_events()
            if action:
                if action == "end_turn":
                    self.end_turn()
                else:
                    self.player_action(action)

            if self.check_game_over():
                running = False

            self.protagonist.display_info(40, 450, 20, 520, 70, 515)
            self.enemy.display_info(300, 10, 330, 80, 380, 18)
            self.display.draw_card_areas()
            self.display.draw_button_areas()
            self.display.draw_hand(self.deck.hand)
            pygame.display.flip()

if __name__ == "__main__":
    game = Main()
    game.run()