import pygame
import random

class asteroid:

    def __init__(self):
        
        self.asteroidImg =[]
        self.asteroidX = []
        self.asteroidY = []
        self.no_of_enemies=4
        self.asteroidY_change = 0.05

        for i in range(self.no_of_enemies):
            self.asteroidImg.append(pygame.image.load("assets/asteroid.png"))
            self.asteroidX.append(random.randint(10, 736))
            self.asteroidY.append(random.randint(-150, -50))

    def update(self):

        for i in range(self.no_of_enemies):
            self.asteroidY[i] += self.asteroidY_change

            # asteroid repositioning
            if self.asteroidY[i] > 600:
                self.asteroidX[i] = random.randint(10, 736)
                self.asteroidY[i] = random.randint(-150, -50)


    def draw(self,screen):

        for i in range(self.no_of_enemies):
            screen.blit(self.asteroidImg[i], (self.asteroidX[i], self.asteroidY[i]))

<<<<<<< HEAD
# ------------------------------------------------------------------
#  LEVEL 2 ENEMY (UFO) — SHOOTS AT PLAYER
# ------------------------------------------------------------------

class Enemy2Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.35
        self.img = pygame.image.load("assets/bullet.png")  # You can add a different bullet

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))


class EnemyLevel2:
    def __init__(self):
        self.img = pygame.image.load("assets/ufo_enemy.png")
        self.x = random.randint(10, 736)
        self.y = random.randint(-120, -50)
        self.x_change = 0.4
        self.shoot_timer = random.randint(100, 180)
        self.bullets = []  # enemy bullets

    def update(self):
        # movement
        self.x += self.x_change
        if self.x <= 0:
            self.x_change = 0.4
        if self.x >= 736:
            self.x_change = -0.4

        # shooting logic
        self.shoot_timer -= 1
        if self.shoot_timer <= 0:
            bullet = Enemy2Bullet(self.x + 20, self.y + 40)
            self.bullets.append(bullet)
            self.shoot_timer = random.randint(100, 180)

        # update bullets
        for b in self.bullets:
            b.update()

        # delete bullets leaving screen
        self.bullets = [b for b in self.bullets if b.y <= 600]

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        for b in self.bullets:
            b.draw(screen)



=======

# class enemy_ship:

#     def __init__():
#         enemy_img =[]
#         enemy_x = []
#         enemy_y = []
#         enemy_bullet=[]
#         e_bullet_x=[]
#         e_bullet_y=[]
#         e_bullet_state=[]
#         no_of_enemies=4

#         for i in range(no_of_enemies):
#             enemy_img.append(pygame.image.load("assets/rockets.png"))
#             enemy_x.append(random.randint(10, 730))
#             enemy_y.append(random.randint(-150, -50))

#             #enemy bullet
#             enemy_bullet.append(pygame.image.load("assets/e_bullet.png"))
#             e_bullet_x.append(enemy_x[i] + 16)
#             e_bullet_y.append(enemy_y[i])
#             e_bullet_state.append("ready")
#         e_bullet_change =0.1
#         enemy_x_change = 0
#         enemy_y_change = 0.05
>>>>>>> d51a490a3e5d0f565af395ae8f4b2cf703f8893d
