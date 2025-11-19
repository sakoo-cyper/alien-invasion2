import pygame
class Settings:

    def __init__(self):
        
        # main screen settings.
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (0, 0, 0 , 150)
        self.bg_image = pygame.image.load("images/cosmos-1866820_1280.jpg")

        #ship settings.
        self.ship_speed = 2
        self.ship_limit = 3

        #bullets settings.
        self.bullet_width = 5
        self.bullet_height =15
        self.bullet_color = ("black")
        self.bullet_speed = 10

        #alien speed
        self.alien_speed = 1
        self.alien_drop_speed = 5
        self.direction = 1

        self.game_over_image = pygame.image.load("images/Screenshot from 2025-06-27 20-22-09.png")