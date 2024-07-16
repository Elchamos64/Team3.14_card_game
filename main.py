import sys
import pygame
from pygame.locals import *
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
        self.sound_manager = Sound()
        self.sound_manager.play_music('Start')

    def end_turn(self):
        if self.protagonist.current_action_points < self.protagonist.max_action_points:
            self.protagonist.current_action_points = self.protagonist.max_action_points
        self.enemy.enemy_action(self.clock, self.protagonist)
        self.deck.draw_cards(3)

    def player_action(self, action):
        if action == "end_turn":
            self.end_turn()
        match(action):
            case "0" | "1" | "2" | "3" | "4":
                Deck.use_card(self.deck, int(action), self.protagonist, self.enemy)
    
    def check_game_over(self):
        if self.protagonist.current_health <= 0:
            self.display.set_background('death')
            self.sound_manager.play_music('Death')
            print("Game Over! Enemy wins!")
            return True

        elif self.enemy.current_health <= 0:
            print("Game Over! Player wins!")
            self.display.set_background('victory')
            self.sound_manager.play_music('Victory')
            return True
        
        else:
            return False

    def main_menu(self):
        self.sound_manager.play_music('Start')
        self.display.set_background('menu')
        self.display.clear_screen()
        # Render main menu text
        font = pygame.font.SysFont(None, 50)
        title_text = font.render("Main Menu", True, (255, 255, 255))  # white color
        play_button_text = pygame.image.load("Images/Display/Play.png")
        play_button_text = pygame.transform.scale(play_button_text, (play_button_text.get_width() * 4, play_button_text.get_height() * 4))
        quit_button_text = pygame.image.load("Images/Display/Quit.png")
        quit_button_text = pygame.transform.scale(quit_button_text, (quit_button_text.get_width() * 4, quit_button_text.get_height() * 4))
        # deck_button_text = font.render("Deck", True, (255, 255, 255))  # white color

        title_rect = title_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 4))
        play_button_rect = play_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        # deck_button_rect = deck_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))
        quit_button_rect = quit_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))

        self.display.screen.blit(title_text, title_rect)
        self.display.screen.blit(play_button_text, play_button_rect)
        # self.display.screen.blit(deck_button_text, deck_button_rect)
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
                    # elif deck_button_rect.collidepoint(mouse_pos):
                    #     return "deck_option"
                    elif quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

    def game_difficulty(self):
        self.display.clear_screen()
        pygame.display.set_caption("Game Difficulty")
        # Render game difficulty text
        font = pygame.font.SysFont(None, 50)
        title_text = font.render("Choose the game difficulty", True, (255, 255, 255))  # white color
        easy_button_text = pygame.image.load("Images/Display/EasyButton.png")
        easy_button_text = pygame.transform.scale(easy_button_text, (easy_button_text.get_width() * 4, easy_button_text.get_height() * 4))
        medium_button_text = pygame.image.load("Images/Display/MediumButton.png")
        medium_button_text = pygame.transform.scale(medium_button_text, (medium_button_text.get_width() * 4, medium_button_text.get_height() * 4))
        hard_button_text = pygame.image.load("Images/Display/HardButton.png")
        hard_button_text = pygame.transform.scale(hard_button_text, (hard_button_text.get_width() * 4,hard_button_text.get_height() * 4))

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
                        self.sound_manager.play_music('Easy')
                        self.enemy.set_enemy('easy')
                        return "deck_option"
                    elif medium_button_rect.collidepoint(mouse_pos):
                        self.sound_manager.play_music('Medium')
                        self.display.set_background('medium')
                        self.enemy.set_enemy('medium')
                        return "deck_option"
                    elif hard_button_rect.collidepoint(mouse_pos):
                        self.sound_manager.play_music('Hard')
                        self.display.set_background('hard')
                        self.enemy.set_enemy('hard')
                        return "deck_option"

    def game_over_screen(self, result):
        self.deck.deck=[]
        self.deck.hand=[]
        self.deck.discard=[]
        self.display.clear_screen()
        pygame.display.set_caption("Game Over")
        # Render game over text
        font = pygame.font.SysFont(None, 50)
        if result == "enemy_wins":
            result_text = font.render("Game Over! Enemy wins!", True, (255, 255, 255))
        else:
            result_text = font.render("Game Over! Player wins!", True, (255, 255, 255))
        play_again_text = pygame.image.load("Images/Display/Play.png")
        play_again_text = pygame.transform.scale(play_again_text, (play_again_text.get_width() * 4, play_again_text.get_height() * 4))
        quit_text = pygame.image.load("Images/Display/Quit.png")
        quit_text = pygame.transform.scale(quit_text, (quit_text.get_width() * 4, quit_text.get_height() * 4))

        result_rect = result_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 4))
        play_again_rect = play_again_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        quit_rect = quit_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))

        self.display.screen.blit(result_text, result_rect)
        self.display.screen.blit(play_again_text, play_again_rect)
        self.display.screen.blit(quit_text, quit_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_again_rect.collidepoint(mouse_pos):
                        self.protagonist.max_health = 100
                        self.protagonist.current_health = 100
                        self.protagonist.current_action_points = 5
                        self.protagonist.max_action_points = 5
                        self.protagonist.block_points = 0 
                        self.enemy.max_health = 50
                        self.enemy.current_health = 50
                        self.enemy.block_points = 25
                        return "main_menu"
                    elif quit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

    def deck_option(self):
        self.display.clear_screen()
        pygame.display.set_caption("Deck Option")
        # Render deck option text
        font = pygame.font.SysFont(None, 50)
        title_text = font.render("Choose the deck", True, (255, 255, 255))  # white color
        fighter_button_text = pygame.image.load("Images/Display/FighterButton.png")
        fighter_button_text = pygame.transform.scale(fighter_button_text, (fighter_button_text.get_width() * 4, fighter_button_text.get_height() * 4))
        ninja_button_text = pygame.image.load("Images/Display/NinjaButton.png")
        ninja_button_text = pygame.transform.scale(ninja_button_text, (ninja_button_text.get_width() * 4, ninja_button_text.get_height() * 4))
        wizard_button_text = pygame.image.load("Images/Display/MagusButton.png")
        wizard_button_text = pygame.transform.scale(wizard_button_text, (wizard_button_text.get_width() * 4, wizard_button_text.get_height() * 4))

        title_rect = title_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 4))
        fighter_button_rect = fighter_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        ninja_button_rect = ninja_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))
        wizard_button_rect = wizard_button_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 100))

        self.display.screen.blit(title_text, title_rect)
        self.display.screen.blit(fighter_button_text, fighter_button_rect)
        self.display.screen.blit(ninja_button_text, ninja_button_rect)
        self.display.screen.blit(wizard_button_text, wizard_button_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if fighter_button_rect.collidepoint(mouse_pos):
                        self.deck.choose_deck('fighter')
                        return "play_fighter"
                    elif ninja_button_rect.collidepoint(mouse_pos):
                        self.deck.choose_deck('ninja')
                        return "play_ninja"
                    elif wizard_button_rect.collidepoint(mouse_pos):
                        self.deck.choose_deck('wizard')
                        return "play_wizard"
    def run(self):
        while True:
            result = self.main_menu()
            if result == "game_difficulty":
                difficulty = self.game_difficulty()
                if difficulty == "deck_option":
                    deck_choice = self.deck_option()
                    if deck_choice in ["play_fighter", "play_ninja", "play_wizard"]:
                        running = True
                        self.deck.draw_initial_hand()
                        self.deck.draw_initial_hand()
                        game_over_result = False
                        while running:
                            self.display.clear_screen()

                            # Handle events
                            action = self.display.handle_events()
                            if action:  # If an action was returned
                                self.player_action(action)

                            # Check for game over
                            game_over_result = self.check_game_over()
                            if game_over_result:
                                running = False
                                end_result = self.game_over_screen(game_over_result)
                                if end_result == "main_menu":
                                    running = False  # Break out of the current loop to return to the main menu

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