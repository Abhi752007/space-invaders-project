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

