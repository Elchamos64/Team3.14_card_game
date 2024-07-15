import pygame
import random
from GameDisplay import GameDisplay  # Assuming this is your display class
from Sound import Sound  # Assuming this is your sound management class
from Protagonist import Protagonist  # Assuming this is your protagonist class

class Enemy(GameDisplay):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.max_health = 150  # Increased max health
        self.current_health = 150
        self.block_points = 30  # Increased block points
        self.attack = False
        self.actions = ["attack", "heal", "block"]
        self.sound_manager = Sound()

        # Images for different enemies and their attacks
        self.enemies = {
            'easy': self.load_and_scale_image('Images/Enemies/MilkJugSteve.png'),
            'medium': self.load_and_scale_image('Images/Enemies/GenericSlimeGeorge.png'),
            'hard': self.load_and_scale_image('Images/Enemies/MimicMaurice.png')
        }
        self.enemyAttacks = {
            'easy': self.load_and_scale_image('Images/Enemies/MilkJugSteveAttack.png'),
            'medium': self.load_and_scale_image('Images/Enemies/GenericSlimeGeorgeAttack.png'),
            'hard': self.load_and_scale_image('Images/Enemies/MimicMauriceAttack.png')
        }

        # Decks for different classes (wizard, ninja, fighter)
        self.decks = {
            'wizard': {'attack': 10, 'heal': 5, 'block': 5},  # Adjusted action weights for wizard
            'ninja': {'attack': 15, 'heal': 3, 'block': 7},   # Adjusted action weights for ninja
            'fighter': {'attack': 5, 'heal': 10, 'block': 10} # Adjusted action weights for fighter
        }

        # Default level and class
        self.current_level = 'hard'  # Start with hard level
        self.current_class = 'wizard'

        # Set initial enemy and attack images
        self.set_enemy(self.current_level)

    def load_and_scale_image(self, image_path):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))

    def set_enemy(self, level):
        if level in self.enemies:
            self.current_enemy = self.enemies[level]
        else:
            raise ValueError(f"No enemy found for level: {level}")

        if level in self.enemyAttacks:
            self.current_enemyAttack = self.enemyAttacks[level]
        else:
            raise ValueError(f"No attack image found for level: {level}")

    def set_class(self, class_name):
        if class_name in self.decks:
            self.current_class = class_name
        else:
            raise ValueError(f"No deck found for class: {class_name}")

    def display_info(self, health_bar_x, health_bar_y, enemy_x, enemy_y, shield_x, shield_y):
        health_bar_width = 200
        health_bar_height = 20
        super().draw_health_bar(self.current_health, self.max_health, health_bar_x, health_bar_y, health_bar_width, health_bar_height)

        health_text = self.font.render(f"{self.current_health}/{self.max_health}", True, (0, 0, 0))
        health_text_x = health_bar_x + (health_bar_width - health_text.get_width()) // 2
        health_text_y = health_bar_y + (health_bar_height - health_text.get_height()) // 2
        self.screen.blit(health_text, (health_text_x, health_text_y))

        if self.attack:
            self.screen.blit(self.current_enemyAttack, (enemy_x, enemy_y))
        else:
            self.screen.blit(self.current_enemy, (enemy_x, enemy_y))

        self.draw_shield_and_block_points(shield_x, shield_y, self.block_points)

    def enemy_action(self, clock, protag):
        action_weights = self.decks[self.current_class]
        action = random.choices(list(action_weights.keys()), weights=list(action_weights.values()), k=1)[0]

        if action == "attack":
            self.attack = True
            damage = random.randint(20, 30)  # Increased damage
            protag.block_points -= damage
            if protag.block_points < 0:
                protag.current_health += protag.block_points
                protag.block_points = 0
                if protag.current_health < 0:
                    protag.current_health = 0
                print(f"Enemy attacks for {damage} damage!")
            self.sound_manager.play_sound('enemy_attack')

        elif action == "heal":
            self.attack = False
            heal_amount = random.randint(5, 10)  # Reduced healing amount
            self.current_health = min(self.max_health, self.current_health + heal_amount)
            print(f"Enemy heals for {heal_amount} health!")

        elif action == "block":
            self.attack = False
            block_points = random.randint(2, 10)  # Reduced block points gain
            self.block_points += block_points
            print(f"Enemy blocks, gaining {block_points} block points!")

    def update(self, clock, protag):
        self.enemy_action(clock, protag)

        # Additional logic for updating enemy state goes here

# Example usage:
# Initialize your game and create an instance of Enemy
pygame.init()
screen_width = 800
screen_height = 600
game_display = GameDisplay(screen_width, screen_height)
enemy = Enemy(screen_width, screen_height)

# Set the enemy level (easy, medium, hard)
enemy.set_enemy('hard')  # Set to hard level

# Set the enemy class (wizard, ninja, fighter)
enemy.set_class('ninja')  # Example class

# Game loop
running = True
clock = pygame.time.Clock()
protagonist = Protagonist()  # Assuming you have a Protagonist class

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game entities
    enemy.update(clock, protagonist)

    # Render game entities
    game_display.display_info(10, 10, 100, 100, 10, 50)  # Example positions
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
SystemError.exit()
