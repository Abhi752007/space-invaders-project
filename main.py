import pygame 
pygame.init()

import player
import bullet
import enemy 
import collision


player = player.player()
enemy = enemy.enemy()
bullet = bullet.bullet()
collision = collision.collision()

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
    #collision.is_collision(enemy.enemyX,enemy.enemyY,bullet.bulletX,bullet.bulletY)

    # Draw
    player.draw(screen)
    enemy.draw(screen)
    bullet.draw(screen)

    pygame.display.update()


