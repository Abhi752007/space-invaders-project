import player
import pygame
from pygame import mixer
mixer.init()
bullet_sound = mixer.Sound("assets/laser.mp3")


class bullet:

    player = player.player()

    def __init__(self):

        self.bulletX = self.player.playerX
        self.bulletY = 480
        self.bulletY_change = 0.2
        self.bullet_state = "ready"
        self.bulletImg = pygame.image.load("assets/bullet.png")

    def fire_bullet(self,playerx):
        self.bullet_state = "fire"
        self.bulletY = 480
        self.bulletX = playerx + 17

    def handle_input(self,event,playerx):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.bullet_state == "ready":
                self.bulletX = playerx + 17
                self.bulletY = 480
                self.fire_bullet(playerx)
                bullet_sound.play()

    def update(self):
        if self.bullet_state == "fire":
            self.bulletY -= self.bulletY_change
            if self.bulletY < 0:
                self.bullet_state = "ready"

    def draw(self,screen):
        if self.bullet_state == "fire":
            screen.blit(self.bulletImg, (self.bulletX, self.bulletY))
