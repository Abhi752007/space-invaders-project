import pygame

class player:

    def __init__(self):
        self.playerImg = None
        self.playerX = 370
        self.playerY = 480
        self.playerX_change = 0
        self.playerImg = pygame.image.load("assets/player.png")

    def handle_input(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                self.playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerX_change = 0

    def update(self):
        self.playerX += self.playerX_change
        if self.playerX < 0:
            self.playerX = 0
        if self.playerX > 736:
            self.playerX = 736

    def draw(self,screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))
