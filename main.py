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
    
    def check_game_over(self):
        if self.protagonist.current_health <= 0:
            print("Game Over! Enemy wins!")
            return True
        elif self.enemy.current_health <= 0:
            print("Game Over! Player wins!")
            return True
        return False

    def main_menu(self):
        self.display.clear_screen()
        pygame.display.set_caption("Main Menu")
        # Render main menu text
        font = pygame.font.SysFont(None, 50)
        title_text = font.render("Main Menu", True, (255, 255, 255))  # Black color
        play_button_text = font.render("Play", True, (255, 255, 255))  # Black color
        quit_button_text = font.render("Quit", True, (255, 255, 255))  # Black color

        title_rect = title_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 4))
        play_button_rect = play_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        quit_button_rect = quit_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))

        self.display.screen.blit(title_text, title_rect)
        self.display.screen.blit(play_button_text, play_button_rect)
        self.display.screen.blit(quit_button_text, quit_button_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_button_rect.collidepoint(mouse_pos):
                        return "game_difficulty"
                    elif quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

    def game_difficulty(self):
        self.display.clear_screen()
        pygame.display.set_caption("Game Difficulty")
        # Render game difficulty text
        font = pygame.font.SysFont(None, 50)
        title_text = font.render("Choose the game difficulty", True, (255, 255, 255))  # Black color
        easy_button_text = font.render("Easy", True, (255, 255, 255))  # Black color
        medium_button_text = font.render("Medium", True, (255, 255, 255))  # Black color
        hard_button_text = font.render("Hard", True, (255, 255, 255))  # Black color

        title_rect = title_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 4))
        easy_button_rect = easy_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        medium_button_rect = medium_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))
        hard_button_rect = hard_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 100))

        self.display.screen.blit(title_text, title_rect)
        self.display.screen.blit(easy_button_text, easy_button_rect)
        self.display.screen.blit(medium_button_text, medium_button_rect)
        self.display.screen.blit(hard_button_text, hard_button_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if easy_button_rect.collidepoint(mouse_pos):
                        self.display.set_background('easy')
                        return "play_easy"
                    elif medium_button_rect.collidepoint(mouse_pos):
                        self.display.set_background('medium')
                        return "play_medium"
                    elif hard_button_rect.collidepoint(mouse_pos):
                        self.display.set_background('hard')
                        return "play_hard"

    def run(self):
        result = self.main_menu()
        if result == "game_difficulty":
            difficulty = self.game_difficulty()
            if difficulty in ["play_easy", "play_medium", "play_hard"]:
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
