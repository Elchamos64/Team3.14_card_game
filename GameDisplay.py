import pygame
import sys
from Card import Card

class GameDisplay:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((255, 255, 255))  # Set screen color to white
        self.card_areas = {}
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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Handle card clicks
                for card_name, area in self.card_areas.items():
                    if area.collidepoint(mouse_pos):
                        print(f"Card clicked: {card_name}")
                        return card_name  # Return the card clicked
                # Handle end turn button
                for button, area in self.button_types.items():
                    if area.collidepoint(mouse_pos):
                        print(f"Button clicked: {button}")
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
        # Draw card holster background
        self.screen.blit(self.card_holster_image, (140, 480))  # Position the background

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

    def draw_hand(self, hand):
        card_width = 60
        card_height = 100
        x = 150
        y = 460
        gap = 20
        
        for card_name in hand:
            if card_name is not None:
                card_image = Card.cards.get(card_name, [None])[0]
                if card_image is not None:
                    # Resize the card image to the desired size
                    card_image = pygame.transform.scale(card_image, (card_width, card_height))
                    
                    # Adjust card position for each card in the hand
                    self.screen.blit(card_image, (x, y))
                    
                    # Increment x position for the next card
                    x += card_width + gap
                else:
                    print(f"Warning: Card image for {card_name} not found.")
            else:
                print("Warning: Card name is None.")