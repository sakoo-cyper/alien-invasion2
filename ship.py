import pygame
class Ship:
    def __init__(self , ai_game):

        self.settings = ai_game.settings
        self.screen = ai_game.surface
        self.screen_rect = ai_game.screen.get_rect()

        self.ship_image = pygame.image.load("images/rocket-306209_1280.png")
        self.rect = self.ship_image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 3

        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def moveing_ship(self):
        if self.move_left and self.rect.x >= 0:
            self.rect.x -= self.settings.ship_speed
        if self.move_right and self.rect.right <= self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.move_up and self.rect.y >= 0:
            self.rect.y -= self.settings.ship_speed
        if self.move_down and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

    def but_ship_img(self):
        self.screen.blit(self.ship_image , self.rect)
        

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 3