import pygame
import player
import random
import collision

#storing all the enemies in lists 
enemy_image = []
enemyX = []
enemyY = []
enemy_x_change = []
enemy_Y_change = []
num_of_enemy = 12


# spawning the enemies
for i in range(num_of_enemy):
    enemy_image.append(pygame.image.load('space-invaders.png'))
    enemyX.append(random.randint(0, 400))
    enemyY.append(random.randint(50, 150))
    enemy_x_change.append(0.3)
    enemy_Y_change.append(0.2)

def player(x,y):
    screen.blit(player.Playerimage, (x, y))

def enemy(x,y):
    screen.blit(enemy_image, (x, y))


# Movement of  enemies
enemy_X_change = []
enemy_Y_change = []
for i in range(num_of_enemy):
    enemyX[i] += enemy_x_change[i]
    if enemyX[i] <= 0:
        enemy_X_change[i] = 4 
        enemyY[i] += enemy_Y_change[i]
    elif enemyX[i] >= 736:
        enemy_X_change[i] = -4 
        enemyY[i] += enemy_Y_change[i]
    
    collsion = collision.iscollsion(enemyX[i], enemyY[i], collision.bulletX, collision.bulletY)
    if player.collsison:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX[i] = random.randint(0,800)
        enemyY[i] = random.randint(50,150)

