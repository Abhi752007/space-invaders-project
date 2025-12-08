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



player = player.player()
asteroid = enemy.asteroid()
bullet = bullet.bullet()
collision = collision.collision()

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


# game_over_screen = True
# def game_over():
#     while game_over_screen:
#         screen.blit(background, (0, 0))
#         over=pygame.font.Font("freesansbold.ttf",64)
#         play_again=pygame.font.Font("freesansbold.ttf",16)
#         over_txt = over.render("GAME OVER", True, (255, 255, 255))
#         play = play_again.render("PLAY AGAIN (y/n)", True, (255, 255, 255))
#         screen.blit(over_txt, (225,250))
#         screen.blit(play, (270, 314))

#         for event in pygame.event.get():
#             if event == pygame.K_y:
#                 running = True
#             if event == pygame.K_y:
#                 running = False      


while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player.handle_input(event)
        bullet.handle_input(event,player.playerX)

    # Update
    player.update()
    asteroid.update()
    bullet.update()


    for i in range(asteroid.no_of_enemies):
        # bullet hits asteroid
        if collision.is_collision(asteroid.asteroidX[i],asteroid.asteroidY[i],bullet.bulletX,bullet.bulletY):
            bullet.bullet_state = "ready"
            #print(45)
            scores += 5

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

    # LEVEL TRANSITION TO LEVEL 2
    if scores >= 500 and not level_triggered:
        ui.show_level_transition(screen, 2)
        level = 2
        level_triggered = True
        asteroid.asteroidY_change = 0.06   # Increase enemy speed in level 2

    # DRAW ELEMENTS
    asteroid.draw(screen)
    bullet.draw(screen)
    player.draw(screen)
    show_score()

    pygame.display.update()
