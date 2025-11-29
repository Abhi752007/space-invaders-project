import pygame
import player
import random

#storing all the enemies in lists 
enemy_image = []
enemy_X = []
enemy_Y = []
enemy_x_change = []
enemy_Y_change = []
num_of_enemy = 12


# spawning the enemies
for i in range(num_of_enemy):
    enemy_image.append(pygame.image.load('space-invaders.png'))
    enemy_X.append(random.randint(0, 400))
    enemy_Y.append(random.randint(50, 150))
    enemy_x_change.append(0.3)
    enemy_Y_change.append(0.2)

def player(x,y):
    screen.blit(Playerimage, (x, y))

def enemy(x,y):
    screen.blit(enemy_image, (x, y))


# Movement of  enemies
for i in range(num_of_enemy):
    enemy_X[i] += enemy_x_change[i]
    if enemy_X[i] <= 0:
        enemy_X_change[i] = 4 
        enemy_Y[i] += enemy_Y_change[i]
    elif enemy_X[i] >= 736:
        enemy_X_change[i] = -4 
        enemy_Y[i] += enemy_Y_change[i]
    
    collsion = iscollsion(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y)
    if collsison:
        bullet_Y = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemy_X[i] = random.randint(0,800)
        enemy_Y[i] = random.randint(50,150)

