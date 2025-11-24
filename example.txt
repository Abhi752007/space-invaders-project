# /* settings.py
WIDTH, HEIGHT = 720, 450

SPACE = 30
FONT_SIZE = 20
EVENT_FONT_SIZE = 60
NAV_THICKNESS = 50
CHARACTER_SIZE  = 30
PLAYER_SPEED = 10
ENEMY_SPEED = 1 
BULLET_SPEED = 15 # for both sides
BULLET_SIZE = 10
# /* main.py
import pygame, sys
from settings import WIDTH, HEIGHT, NAV_THICKNESS
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + NAV_THICKNESS))
pygame.display.set_caption("Space Invader")

class Main:
    def _init_(self, screen):
        self.screen = screen
        self.FPS = pygame.time.Clock()

    def main(self):
        world = World(self.screen)
        while True:
            self.screen.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        world.player_move(attack = True)
            world.player_move()
            world.update()
            pygame.display.update()
            self.FPS.tick(30)

if _name_ == "_main_":
    play = Main(screen)
    play.main()
# /* ship.py
import pygame
from settings import PLAYER_SPEED, BULLET_SIZE
from bullet import Bullet

class Ship(pygame.sprite.Sprite):
    def _init_(self, pos, size):
        super()._init_()
        self.x = pos[0]
        self.y = pos[1]
        # ship info 
        img_path = 'assets/ship/ship.png'
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.ship_speed = PLAYER_SPEED
        # ship status
        self.life = 3
        self.player_bullets = pygame.sprite.Group()

    def move_left(self):
        self.rect.x -= self.ship_speed

    def move_up(self):
        self.rect.y -= self.ship_speed

    def move_right(self):
        self.rect.x += self.ship_speed

    def move_bottom(self):
        self.rect.y += self.ship_speed

    def _shoot(self):
        specific_pos = (self.rect.centerx - (BULLET_SIZE // 2), self.rect.y)
        self.player_bullets.add(Bullet(specific_pos, BULLET_SIZE, "player"))

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
# /* alien.py
import pygame
from settings import BULLET_SIZE
from bullet import Bullet

class Alien(pygame.sprite.Sprite):
    def _init_(self, pos, size, row_num):
        super()._init_()
        self.x = pos[0]
        self.y = pos[1]
        # alien info
        img_path = f'assets/aliens/{row_num}.png'
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.move_speed = 5
        self.to_direction = "right"
        # alien status
        self.bullets = pygame.sprite.GroupSingle()

    def move_left(self):
        self.rect.x -= self.move_speed

    def move_right(self):
        self.rect.x += self.move_speed

    def move_bottom(self):
        self.rect.y += self.move_speed

    def _shoot(self):
        specific_pos = (self.rect.centerx - (BULLET_SIZE // 2), self.rect.centery)
        self.bullets.add(Bullet(specific_pos, BULLET_SIZE, "enemy"))

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
# /* bullet.py
import pygame
from settings import BULLET_SPEED, HEIGHT

class Bullet(pygame.sprite.Sprite):
    def _init_(self, pos, size, side):
        super()._init_()
        self.x = pos[0]
        self.y = pos[1]
        # bullet info
        img_path = f'assets/bullet/{side}-bullet.png'
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)
        # different bullet movement direction for both player and enemy (alien)
        if side == "enemy":
            self.move_speed = BULLET_SPEED
        elif side == "player":
            self.move_speed = (- BULLET_SPEED)

    def _move_bullet(self):
        self.rect.y += self.move_speed

    def update(self):
        self._move_bullet()
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        # delete the bullet if it get through out of the screen
        if self.rect.bottom <= 0 or self.rect.top >= HEIGHT:
            self.kill()
# /* world.py
import pygame
from ship import Ship
from alien import Alien
from settings import HEIGHT, WIDTH, ENEMY_SPEED, CHARACTER_SIZE, BULLET_SIZE, NAV_THICKNESS
from bullet import Bullet
from display import Display

class World:
    def _init_(self, screen):
        self.screen = screen
        self.player = pygame.sprite.GroupSingle()
        self.aliens = pygame.sprite.Group()
        self.display = Display(self.screen)
        self.game_over = False
        self.player_score = 0
        self.game_level = 1
        self._generate_world()
# /* world.py
    def _generate_aliens(self):
        # generate opponents
        alien_cols = (WIDTH // CHARACTER_SIZE) // 2
        alien_rows = 3
        for y in range(alien_rows):
            for x in range(alien_cols):
                my_x = CHARACTER_SIZE * x
                my_y = CHARACTER_SIZE * y
                specific_pos = (my_x, my_y)
                self.aliens.add(Alien(specific_pos, CHARACTER_SIZE, y))
        
    # create and add player to the screen
    def _generate_world(self):
        # create the player's ship
        player_x, player_y = WIDTH // 2, HEIGHT - CHARACTER_SIZE
        center_size = CHARACTER_SIZE // 2
        player_pos = (player_x - center_size, player_y)
        self.player.add(Ship(player_pos, CHARACTER_SIZE))
        self._generate_aliens()
# /* world.py
    def add_additionals(self):
        # add nav bar
        nav = pygame.Rect(0, HEIGHT, WIDTH, NAV_THICKNESS)
        pygame.draw.rect(self.screen, pygame.Color("gray"), nav)
        # render player's life, score and game level
        self.display.show_life(self.player.sprite.life)
        self.display.show_score(self.player_score)
        self.display.show_level(self.game_level)
# /* world.py
    def player_move(self, attack = False):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and not self.game_over or keys[pygame.K_LEFT] and not self.game_over:
            if self.player.sprite.rect.left > 0:
                self.player.sprite.move_left()
        if keys[pygame.K_d] and not self.game_over or keys[pygame.K_RIGHT] and not self.game_over:
            if self.player.sprite.rect.right < WIDTH:
                self.player.sprite.move_right()
        if keys[pygame.K_w] and not self.game_over or keys[pygame.K_UP] and not self.game_over:
            if self.player.sprite.rect.top > 0:
                self.player.sprite.move_up()		
        if keys[pygame.K_s] and not self.game_over or keys[pygame.K_DOWN] and not self.game_over:
            if self.player.sprite.rect.bottom < HEIGHT:
                self.player.sprite.move_bottom()
        # game restart button
        if keys[pygame.K_r]:
            self.game_over = False
            self.player_score = 0
            self.game_level = 1
            for alien in self.aliens.sprites():
                alien.kill()
            self._generate_world()
        if attack and not self.game_over:
            self.player.sprite._shoot()
# /* world.py
    def _detect_collisions(self):
        # checks if player bullet hits the enemies (aliens)
        player_attack_collision = pygame.sprite.groupcollide(self.aliens, self.player.sprite.player_bullets, True, True)
        if player_attack_collision:
            self.player_score += 10
        # checks if the aliens' bullet hit the player
        for alien in self.aliens.sprites():	
            alien_attack_collision = pygame.sprite.groupcollide(alien.bullets, self.player, True, False)
            if alien_attack_collision:
                self.player.sprite.life -= 1
                break
        # checks if the aliens hit the player
        alien_to_player_collision = pygame.sprite.groupcollide(self.aliens, self.player, True, False)
        if alien_to_player_collision:
            self.player.sprite.life -= 1
# /* world.py
    def _alien_movement(self):
        move_sideward = False
        move_forward = False
        for alien in self.aliens.sprites():
            if alien.to_direction == "right" and alien.rect.right < WIDTH or alien.to_direction == "left" and alien.rect.left > 0:
                move_sideward = True
                move_forward = False
            else:
                move_sideward = False
                move_forward = True
                alien.to_direction = "left" if alien.to_direction == "right" else "right"
                break
        for alien in self.aliens.sprites():
            if move_sideward and not move_forward:
                if alien.to_direction == "right":
                    alien.move_right()
                if alien.to_direction == "left":
                    alien.move_left()
            if not move_sideward and move_forward:
                    alien.move_bottom()

    def _alien_shoot(self):
        for alien in self.aliens.sprites():
            if (WIDTH - alien.rect.x) // CHARACTER_SIZE == (WIDTH - self.player.sprite.rect.x) // CHARACTER_SIZE:
                alien._shoot()
                break
# /* world.py
    def _check_game_state(self):
        # check if game over
        if self.player.sprite.life <= 0:
            self.game_over = True
            self.display.game_over_message()
        for alien in self.aliens.sprites():
            if alien.rect.top >= HEIGHT:
                self.game_over = True
                self.display.game_over_message()
                break
        # check if next level
        if len(self.aliens) == 0 and self.player.sprite.life > 0:
            self.game_level += 1
            self._generate_aliens()
            for alien in self.aliens.sprites():
                alien.move_speed += self.game_level - 1
# /* world.py
    def update(self):
        # detecting if bullet, alien, and player group is colliding
        self._detect_collisions()
        # allows the aliens to move
        self._alien_movement()
        # allows alien to shoot the player
        self._alien_shoot()
        # bullets rendering
        self.player.sprite.player_bullets.update()
        self.player.sprite.player_bullets.draw(self.screen)
        [alien.bullets.update() for alien in self.aliens.sprites()]
        [alien.bullets.draw(self.screen) for alien in self.aliens.sprites()]
        # player ship rendering
        self.player.update()
        self.player.draw(self.screen)
        # alien rendering
        self.aliens.draw(self.screen)
        # add nav
        self.add_additionals()
        # checks game state
        self._check_game_state()
# /* display.py
import pygame
from settings import WIDTH, HEIGHT, SPACE, FONT_SIZE, EVENT_FONT_SIZE

pygame.font.init()

class Display:
    def _init_(self, screen):
        self.screen = screen
        self.score_font = pygame.font.SysFont("monospace", FONT_SIZE)
        self.level_font = pygame.font.SysFont("impact", FONT_SIZE)
        self.event_font = pygame.font.SysFont("impact", EVENT_FONT_SIZE)
        self.text_color = pygame.Color("blue")
        self.event_color = pygame.Color("red")

    def show_life(self, life):
        life_size = 30
        img_path = "assets/life/life.png"
        life_image = pygame.image.load(img_path)
        life_image = pygame.transform.scale(life_image, (life_size, life_size))
        life_x = SPACE // 2
        if life != 0:
            for life in range(life):
                self.screen.blit(life_image, (life_x, HEIGHT + (SPACE // 2)))
                life_x += life_size

    def show_score(self, score):
        score_x = WIDTH // 3
        score = self.score_font.render(f'score: {score}', True, self.text_color)
        self.screen.blit(score, (score_x, (HEIGHT + (SPACE // 2))))

    def show_level(self, level):
        level_x = WIDTH // 3
        level = self.level_font.render(f'Level {level}', True, self.text_color)
        self.screen.blit(level, (level_x * 2, (HEIGHT + (SPACE // 2))))

    def game_over_message(self):
        message = self.event_font.render('GAME OVER!!', True, self.event_color)
        self.screen.blit(message, ((WIDTH // 3) - (EVENT_FONT_SIZE // 2), (HEIGHT // 2) - (EVENT_FONT_SIZE // 2)))