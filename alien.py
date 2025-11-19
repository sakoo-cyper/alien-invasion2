import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/result_ufo-6961493_1280.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        

    def check_edge(self):
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0 :
            return True
        

    def update(self):
        self.rect.x += (self.settings.alien_speed * self.settings.direction)


