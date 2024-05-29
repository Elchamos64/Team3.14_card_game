import pygame
import sys

class GameDisplay:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((255, 255, 255))  # Set screen color to white
        pygame.display.set_caption("Card Game")

        # Set icon
        icon = pygame.image.load("Images/Display/Heart.png")
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

        # Load and scale shield image
        self.shield_image = pygame.image.load("Images/Enemies/Shield.png")
        self.shield_image = pygame.transform.scale(self.shield_image, (self.shield_image.get_width() * 4, self.shield_image.get_height() * 4))  # Adjust the size as needed

        # Define card areas
        self.card_areas = {
            "attack": pygame.Rect(50, 500, 100, 50),
            "heal": pygame.Rect(200, 500, 100, 50),
            "block": pygame.Rect(350, 500, 100, 50),
        }

        # Define button areas
        self.button_areas = {
            self.end_turn_button: pygame.Rect(600, 500, 144, 45),
        }
        self.button_types = {
            "end_turn": pygame.Rect(600, 500, 144, 45),
        }

    def clear_screen(self):
        self.screen.fill((255, 255, 255))  # Clear screen to white

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

    def draw_shield_and_block_points(self, shield_x, shield_y, block_points):
        # Draw the shield image
        self.screen.blit(self.shield_image, (shield_x, shield_y))

        # Render block points text
        block_points_text = self.font.render(str(block_points), True, (0, 0, 0))  # Black color
        text_rect = block_points_text.get_rect(center=(shield_x + self.shield_image.get_width() // 2, shield_y + self.shield_image.get_height() // 2))

        # Blit block points text
        self.screen.blit(block_points_text, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Handle card areas
                for card, area in self.card_areas.items():
                    if area.collidepoint(mouse_pos):
                        return card  # Return the card clicked
                # Handle End turn
                for button, area in self.button_types.items():
                    if area.collidepoint(mouse_pos):
                        return button  # Return the button clicked

    def update_display(self):
        pygame.display.flip()

    def get_screen(self):
        return self.screen

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    
    def draw_card_areas(self):
        for area in self.card_areas.values():
            pygame.draw.rect(self.screen, (0, 0, 0), area, 2)  # Draw card areas as rectangles

    def draw_button_areas(self):
        for key in self.button_areas.keys():
            self.screen.blit(key, (self.button_areas.get(key).left, self.button_areas.get(key).top))