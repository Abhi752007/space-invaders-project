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