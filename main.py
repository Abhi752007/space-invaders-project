import pygame 
pygame.init()

import random
import player
import bullet
import enemy 
import collision


player = player.player()
enemy = enemy.enemy()
bullet = bullet.bullet()
collision = collision.collision()

score = 0

screen = pygame.display.set_mode((800, 600))
running = True


while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player.handle_input(event)
        bullet.handle_input(event,player.playerX)

    # Update
    player.update()
    enemy.update()
    bullet.update()


    for i in range(enemy.no_of_enemies):

        if collision.is_collision(enemy.enemyX[i],enemy.enemyY[i],bullet.bulletX,bullet.bulletY):
            bullet.bullet_state = "ready"
            print(45)
            score += 5
            enemy.enemyX[i] = random.randint(10, 736)
            enemy.enemyY[i] = random.randint(-150, -50)


    # Draw
    enemy.draw(screen)
    bullet.draw(screen)
    player.draw(screen)

    pygame.display.update()


