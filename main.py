import pygame
import player
import bullet
import enemy 
import collision

pygame.init()

player = player.player()
enemy = enemy.enemy()
bullet = bullet.bullet()

screen = pygame.display.set_mode((800, 600))
running = True


while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player.handle_input(event)
        bullet.handle_input(event)

    # Update
    player.update()
    enemy.update()
    bullet.update()

    # Draw
    player.draw(screen)
    enemy.draw(screen)
    bullet.draw(screen)

    pygame.display.update()


