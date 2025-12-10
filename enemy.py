import pygame
import bullet
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

class enemyShip:

    def __init__(self):
        self.enemyImg =[]
        self.enemyShipX = []
        self.enemyShipY = []
        self.e_bulletImg = []
        self.bullet_state = []
        self.bulletX = []
        self.bulletY = []
        self.no_of_enemies=4
        self.enemyShipY_change = 0.05
        self.bulletY_change = 0.1

        for i in range(self.no_of_enemies):
            self.enemyImg.append(pygame.image.load("assets/rocket.png"))
            self.enemyShipX.append(random.randint(10, 736))
            self.enemyShipY.append(random.randint(-150, -100))

            # Enemy bullet
            self.bulletX.append(self.enemyShipX[i])
            self.bulletY.append(self.enemyShipY[i])
            self.bullet_state.append("ready")
            self.e_bulletImg.append(pygame.image.load("assets/e_bullet.png"))

    def update(self):

        for i in range(self.no_of_enemies):
            # vertical movement
            self.enemyShipY[i] += self.enemyShipY_change

            # fire bullet downward
            if self.bullet_state[i] == "ready":
                self.bullet_state[i] = "fire"
                self.bulletY[i] = self.enemyShipY[i]
                self.bulletX[i] = self.enemyShipX[i] + 15

            if self.bullet_state[i] == "fire":
                self.bulletY[i] += self.bulletY_change
                if self.bulletY[i] > 600:
                    self.bullet_state[i] = "ready"

            if self.enemyShipY[i] > 600:
                self.enemyShipX[i] = random.randint(10, 736)
                self.enemyShipY[i] = random.randint(-150, -100)
                self.bullet_state[i] = "ready"
                self.bulletX[i] = self.enemyShipX[i]
                self.bulletY[i] = self.enemyShipY[i]


    def draw(self,screen):
        for i in range(self.no_of_enemies):
            screen.blit(self.e_bulletImg[i], (self.bulletX[i], self.bulletY[i]))
            screen.blit(self.enemyImg[i], (self.enemyShipX[i], self.enemyShipY[i]))
