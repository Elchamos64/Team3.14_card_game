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
        self.grey_heart_image = pygame.transform.scale(self.grey_heart_image, (self.grey_heart_image.get_width() * 4.5, self.grey_heart_image.get_height()* 4.5))
        self.red_heart_image = pygame.transform.scale(self.red_heart_image, (self.red_heart_image.get_width() * 4.5, self.red_heart_image.get_height() * 4.5))

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

    def update_display(self):
        pygame.display.flip()

    def get_screen(self):
        return self.screen

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height