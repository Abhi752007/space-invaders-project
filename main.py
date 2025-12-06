import pygame 
pygame.init()
#import scores
import random
import player
import bullet
import enemy 
import collision


font = pygame.font.Font(None, 32)

background = pygame.image.load("assets/bg3.png")
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/ufo.png")
player = player.player()
enemy = enemy.enemy()
bullet = bullet.bullet()
collision = collision.collision()
screen = pygame.display.set_mode((800, 600))
running = True
def show_score():
    score_text = font.render(f"Score: {scores}", True, (255, 255, 255))  # white color
    screen.blit(score_text, (10, 10))  # top-left corner

scores=0
while running:
    screen.blit(background, (0, 0))

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
            #print(45)
            scores += 5

            enemy.enemyX[i] = random.randint(10, 736)
            enemy.enemyY[i] = random.randint(-150, -50)

    # Draw
    enemy.draw(screen)
    bullet.draw(screen)
    player.draw(screen)
    show_score()

    pygame.display.update()


