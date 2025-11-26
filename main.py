#SPACE INVADERS

import pygame

pygame.init()

running = True

# display
HEIGHT = 600
WIDTH = 800
game_name = "Space Invaders"
pygame.display.set_caption(game_name)
#game_icon = pygame.image.load("rocket.png")
#pygame.display.set_icon(game_icon)
screen = pygame.display.set_mode((WIDTH,HEIGHT))


while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        # To close the window
        if event.type == pygame.QUIT:
            running = False

