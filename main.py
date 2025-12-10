import pygame 
pygame.init()
from pygame import mixer
mixer.init()
#import scores
import random
import player
import bullet
import enemy 
import collision
import ui


# creating objects
player = player.player()
asteroid = enemy.asteroid()
enemyShip = enemy.enemyShip()
bullet = bullet.bullet()
collision = collision.collision()

# display
font = pygame.font.Font(None, 32)
background = pygame.image.load("assets/bg3.png")
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/ufo.png")
bullet_sound = mixer.Sound("assets/laser.mp3")
screen = pygame.display.set_mode((800, 600))

running = True


def show_score():
    score_text = font.render(f"Score: {scores}", True, (255, 255, 255))  # white color
    screen.blit(score_text, (10, 10))  # top-left corner
scores=0 
level = 1


# main loop
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player.handle_input(event)
        bullet.handle_input(event,player.playerX)

    # Update
    player.update()
    bullet.update()

    if level == 1: # checking currently if level 1 

        level_triggered = False
        for i in range(asteroid.no_of_enemies):
            # bullet hits asteroid
            if collision.is_collision(asteroid.asteroidX[i],asteroid.asteroidY[i],bullet.bulletX,bullet.bulletY):
                bullet.bullet_state = "ready"
                #print(45)
                scores += 25

                asteroid.asteroidX[i] = random.randint(10, 736)
                asteroid.asteroidY[i] = random.randint(-150, -50)

            if collision.is_collision(
                    asteroid.asteroidX[i], asteroid.asteroidY[i],
                    player.playerX, player.playerY):

                play_again = ui.game_over_screen(screen, scores)

                if play_again:
                    # RESET GAME
                    scores = 0
                    level = 1
                    level_triggered = False

                    player = player.__class__()
                    asteroid = enemy.asteroid()
                    bullet = bullet.__class__()

                    continue
                else:
                    running = False

        # level transition
        if scores >= 500 and not level_triggered:
            ui.show_level_transition(screen, 2)
            level = 2
            level_triggered = True

        asteroid.update()
        asteroid.draw(screen)

    if level == 2: # checking currently if level 2

        # player bullet and enemy collision
        for i in range(enemyShip.no_of_enemies):
            # bullet hits enemy ship
            if collision.is_collision(enemyShip.enemyShipX[i],enemyShip.enemyShipY[i],bullet.bulletX,bullet.bulletY):
                bullet.bullet_state = "ready"
                #print(45)
                scores += 25

                enemyShip.enemyShipX[i] = random.randint(10, 736)
                enemyShip.enemyShipY[i] = random.randint(-150, -100)
                enemyShip.bullet_state[i] = "ready"
                enemyShip.bulletX[i] = enemyShip.enemyShipX[i]
                enemyShip.bulletY[i] = enemyShip.enemyShipY[i]

            # if enemy or its bullet collide with player
            if collision.is_collision(
                        enemyShip.enemyShipX[i], enemyShip.enemyShipY[i],
                        player.playerX, player.playerY) or collision.is_collision(enemyShip.bulletX[i],enemyShip.bulletY[i],player.playerX, player.playerY):

                    play_again = ui.game_over_screen(screen, scores)

                    if play_again:
                        # RESET GAME
                        scores = 0
                        level = 1
                        level_triggered = False

                        player = player.__class__()
                        asteroid = enemy.asteroid()
                        enemyShip = enemy.enemyShip()
                        bullet = bullet.__class__()

                        continue
                    else:
                        running = False
        
        enemyShip.update()
        enemyShip.draw(screen)


    # draw elements
    bullet.draw(screen)
    player.draw(screen)

    show_score()

    pygame.display.update()
    