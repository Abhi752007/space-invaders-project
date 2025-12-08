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



