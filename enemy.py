import pygame
import random

class enemy:

    def __init__(self):
        self.enemyX = 0
        self.enemyY = 0
        self.enemyY_change = 0.2
        self.enemyImg = pygame.image.load("assets/asteroid.png")
        self.enemyX = random.randint(0, 736)
        self.enemyY = random.randint(50, 150)

    def update(self):
        self.enemyY += self.enemyY_change


    def draw(self,screen):
        screen.blit(self.enemyImg, (self.enemyX, self.enemyY))

