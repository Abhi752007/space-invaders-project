import pygame
import inspect, os

print(">>> scores.py LOADED from:", os.path.abspath(__file__))

print(">>> Names inside this module:", dir())

class Score:
    # Initialize the Score class with default values.
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 32)

    def add(self, points):
        self.value += points

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.value}", True, (255,255,255))
        screen.blit(score_text, (10,10))
