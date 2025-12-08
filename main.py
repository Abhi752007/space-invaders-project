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

        # asteroid hits the player
        if collision.is_collision(asteroid.asteroidX[i],asteroid.asteroidY[i],player.playerX,player.playerY):
            bullet.bullet_state = "ready"
            # running = False
            # game_over()



        
    
    # Draw
    asteroid.draw(screen)
    bullet.draw(screen)
    player.draw(screen)
    show_score()

    pygame.display.update()

