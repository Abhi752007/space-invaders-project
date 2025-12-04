import player
import pygame

class bullet:

    player = player.player()

    def __init__(self):
        
        self.bulletX = 0
        self.bulletY = 480
        self.bulletY_change = 0.2
        self.bullet_state = "ready"
        self.bulletImg = pygame.image.load("assets/bullet.png")

    def fire_bullet(self):
        self.bullet_state = "fire"
        self.bulletY = 480
        self.bulletX = self.player.playerX

    def handle_input(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.bullet_state == "ready":

                self.bulletX = self.player.playerX
                self.fire_bullet()

    def update(self):
        if self.bullet_state == "fire":
            self.bulletY -= self.bulletY_change
            if self.bulletY < 0:
                self.bullet_state = "ready"

    def draw(self,screen):
        if self.bullet_state == "fire":
            screen.blit(self.bulletImg, (self.bulletX, self.bulletY))
