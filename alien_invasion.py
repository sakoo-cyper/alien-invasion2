import pygame
from time import sleep
from settings import Settings
from game_states import GameState
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    pygame.init()

    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        self.surface = pygame.Surface((self.settings.screen_width , self.settings.screen_height) , pygame.SRCALPHA)
        self.state = GameState(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (self.settings.bg_color)
        flag = True

        while flag:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        flag = False
                    if event.key == pygame.K_ESCAPE:
                        flag = False
                    self._key_down_events(event)
                if event.type == pygame.KEYUP:
                    self._key_up_events(event)

            self._update_screen()
            
            if self.state.active_flag:
                self._update_bullets()
                self._update_alien_movement()
                if not self.aliens:
                    self._create_fleet()
                    self.settings.alien_speed += 1
                    self.settings.alien_drop_speed +=1
                    for alien in self.aliens.sprites():
                        alien.rect.y -= 400
                        # self._update_alien_movement()
                        
                        
    

    def _hit_alien_ship(self):

        if self.state.ship_left > 0 :
            self.state.ship_left -=1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            for alien in self.aliens.sprites():
                alien.rect.y -= 400
            self.ship.center_ship()

            sleep(0.1)

        else :
            self.state.active_flag = False
            
            




    def _update_alien_movement(self):
         self._check_screen_edge()
         self.aliens.update()
         self.screen_rect = self.screen.get_rect()
         if pygame.sprite.spritecollideany(self.ship , self.aliens):
             self._hit_alien_ship()
         for alien in self.aliens.sprites():
             if alien.rect.bottom >= self.screen_rect.bottom:
                 self._hit_alien_ship()
                 break


    def _check_screen_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_direction()
                break


    def _change_direction(self):
        for alien in self.aliens.sprites():
              alien.rect.y += self.settings.alien_drop_speed
        self.settings.direction *= -1


    def _create_fleet(self):
            new_alien = Alien(self) 
            alien_space_width = self.settings.screen_width - (2 * new_alien.rect.width)
            alien_number = alien_space_width // (2 * new_alien.rect.width)

            alien_space_height = self.settings.screen_height - ((2 * new_alien.rect.height) + self.ship.rect.height)
            alien_row_number = alien_space_height // (2 * new_alien.rect.height)
            for alien_row in range(alien_row_number):
                for alien in range(alien_number):
                    self._create_aline(alien , alien_row)


    def _create_aline(self , alien , alien_row):
            new_alien = Alien(self)
            new_alien.rect.x = new_alien.rect.width + (2 * new_alien.rect.width * alien)
            new_alien.rect.y = new_alien.rect.height + (2 * new_alien.rect.height * alien_row)
            self.aliens.add(new_alien)     

                    
    def _key_down_events(self , event):
        if event.key == pygame.K_a:
            self.ship.move_left = True
        if event.key == pygame.K_d:
            self.ship.move_right = True
        if event.key == pygame.K_w:
            self.ship.move_up = True
        if event.key == pygame.K_s:
            self.ship.move_down = True

        # elif event.key == pygame.K_LEFT:
        #     self.ship.move_left = True
        # elif event.key == pygame.K_RIGHT:
        #     self.ship.move_right = True
        # elif event.key == pygame.K_UP:
        #     self.ship.move_up = True
        # elif event.key == pygame.K_DOWN:
        #     self.ship.move_down = True
    
        if event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):

        self.bullets.update()
        #check for any collisions occure.
        collisions = pygame.sprite.groupcollide(self.bullets , self.aliens , True ,True)
        for bullet in self.bullets.sprites():
            if bullet.y <= 0:
                self.bullets.remove(bullet)


    def _key_up_events(self , event):
        if event.key == pygame.K_a:
            self.ship.move_left = False
        if event.key == pygame.K_d:
            self.ship.move_right = False
        if event.key == pygame.K_w:
            self.ship.move_up = False
        if event.key == pygame.K_s:
            self.ship.move_down = False


    def _update_screen(self):

        self.ship.moveing_ship()

        if self.state.active_flag:
            self.screen.blit( self.settings.bg_image , self.screen.get_rect())
        else:
            self.aliens.empty()
            self.bullets.empty()
            self.screen.blit( self.settings.game_over_image , self.screen.get_rect())

        self.screen.blit(self.surface , (0,0))
        pygame.draw.rect(self.surface , self.bg_color ,self.screen.get_rect() )
        # self.screen.fill(self.bg_color)
        self.aliens.draw(self.surface)
        self.ship.but_ship_img()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    ai_game = AlienInvasion()