import pygame
import random

class enemy:

    def __init__(self):
        
        self.enemyImg =[]
        self.enemyX = []
        self.enemyY = []
        self.no_of_enemies=4
        self.enemyY_change = 0.05

        for i in range(self.no_of_enemies):
            self.enemyImg.append(pygame.image.load("assets/asteroid.png"))
            self.enemyX.append(random.randint(10, 736))
            self.enemyY.append(random.randint(-150, -50))

    def update(self):

        for i in range(self.no_of_enemies):
            self.enemyY[i] += self.enemyY_change

            # enemy repositioning
            if self.enemyY[i] > 600:
                self.enemyX[i] = random.randint(10, 736)
                self.enemyY[i] = random.randint(-150, -50)


    def draw(self,screen):

        for i in range(self.no_of_enemies):
            screen.blit(self.enemyImg[i], (self.enemyX[i], self.enemyY[i]))

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



