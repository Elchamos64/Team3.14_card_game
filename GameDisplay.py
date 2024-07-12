import pygame
import sys
from Sound import Sound

class GameDisplay:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.card_areas = {}
        self.screen.fill((255, 255, 255))  # Set screen color to white
        pygame.display.set_caption("Deck Dungeon")
        self.sound_manager = Sound()

        # Set icon
        icon = pygame.image.load("Images/Display/CardBack.png")
        pygame.display.set_icon(icon)

        # Font for displaying text
        self.font = pygame.font.SysFont(None, 20)

        # Load heart images and scale them down
        self.grey_heart_image = pygame.image.load("Images/Display/UnfilledHeart.png")
        self.red_heart_image = pygame.image.load("Images/Display/Heart.png")
        self.grey_heart_image = pygame.transform.scale(self.grey_heart_image, (self.grey_heart_image.get_width() * 4.5, self.grey_heart_image.get_height() * 4.5))
        self.red_heart_image = pygame.transform.scale(self.red_heart_image, (self.red_heart_image.get_width() * 4.5, self.red_heart_image.get_height() * 4.5))

        # Load buttons
        self.end_turn_button = pygame.image.load("Images/Display/EndTurn.png")
        self.end_turn_button = pygame.transform.scale(self.end_turn_button, (self.end_turn_button.get_width() * 3, self.end_turn_button.get_height() * 3))

        # Load shield image and scale it
        self.shield_image = pygame.image.load("Images/Display/Shield.png")
        self.shield_image = pygame.transform.scale(self.shield_image, (self.shield_image.get_width() * 4, self.shield_image.get_height() * 4))

        # Load card holster background
        self.card_holster_image = pygame.image.load("Images/Display/CardHolster.png")
        self.card_holster_image = pygame.transform.scale(self.card_holster_image, (420, 100))  # Adjust size as needed

        # Define button areas
        self.button_areas = {
            self.end_turn_button: pygame.Rect(600, 500, 144, 45),
        }
        self.button_types = {
            "end_turn": pygame.Rect(600, 500, 144, 45),
        }
        self.card_areas = {
            "0": pygame.Rect(150, 480, 65, 85),
            "1": pygame.Rect(220, 480, 65, 85),
            "2": pygame.Rect(290, 480, 65, 85),
            "3": pygame.Rect(360, 480, 65, 85),
            "4": pygame.Rect(430, 480, 65, 85),
        }

    # Background management
        self.backgrounds = {
            'menu': self.load_and_scale_image('Images/Display/Menu.png'),
            'easy': self.load_and_scale_image('Images/Display/Easy.png'),
            'medium': self.load_and_scale_image('Images/Display/Medium.png'),
            'hard' : self.load_and_scale_image('Images/Display/Hard.png'),
            'victory' : self.load_and_scale_image('Images/Display/victory.png'),
            'death' : self.load_and_scale_image('Images/Display/dead.png')
        }
        self.current_background = self.backgrounds['menu']  # Default background

    def load_and_scale_image(self, image_path):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (self.width, self.height))
    
    def set_background(self, level):
        if level in self.backgrounds:
            self.current_background = self.backgrounds[level]
        else:
            raise ValueError(f"No background found for level: {level}")

    def clear_screen(self):
        self.screen.blit(self.current_background, (0, 0))  # Draw the background image

    def draw_health_bar(self, current_health, max_health, x, y, width, height):
        # Draw grey heart (background)
        self.screen.blit(self.grey_heart_image, (x, y))

        # Calculate health percentage
        health_percentage = current_health / max_health

        # Calculate height of clipping region based on health percentage
        height = int(self.red_heart_image.get_height())

        # Set clipping region for red heart image
        clipping_rect = pygame.Rect(x, y + (height * (1 - health_percentage)), width, height)
        self.screen.set_clip(clipping_rect)

        # Draw red heart (represents current health)
        self.screen.blit(self.red_heart_image, (x, y))

        # Reset clipping region
        self.screen.set_clip(None)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Handle card areas
                for card_index, area in self.card_areas.items():
                    if area.collidepoint(mouse_pos):
                        print(f"Card clicked: {card_index}")
                        return card_index  # Return the card clicked as string
                # Handle End turn button
                for button, area in self.button_areas.items():
                    if area.collidepoint(mouse_pos):
                        return "end_turn"  # Return "end_turn" if end turn button is clicked
        return None

    def update_display(self):
        pygame.display.flip()

    def get_screen(self):
        return self.screen

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    
    def draw_card_areas(self, deck):
        # Draw card holster background
        self.screen.blit(self.card_holster_image, (150, 480))  # Position the background
        deck.draw_card_areas(self.screen)

    def draw_button_areas(self):
        for key in self.button_areas.keys():
            self.screen.blit(key, (self.button_areas.get(key).left, self.button_areas.get(key).top))

    def draw_shield_and_block_points(self, shield_x, shield_y, block_points):
        # Draw the shield image
        self.screen.blit(self.shield_image, (shield_x, shield_y))

        # Render block points text
        block_points_text = self.font.render(str(block_points), True, (0, 0, 0))  # Black color
        text_rect = block_points_text.get_rect(center=(shield_x + self.shield_image.get_width() // 2, shield_y + self.shield_image.get_height() // 2))

        # Blit block points text
        self.screen.blit(block_points_text, text_rect)
