# Bullet module for player projectiles
import random
import pygame

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImage = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480 # initial position of the bullet (same as player Y position)
bulletY_change = 10
bullet_state = "ready" # changing the state of the bullet

# Function to fire the bullet
def fire_bullet(x, y):
    global bullet_state # global is a keyword which is used to access the variable outside the function
    bullet_state = "fire" # changing the state of the fire
    screen.blit(bulletImage,(x + 16, y + 10)) # x+16 to center the bullet on the player and y+10 to position it above the player

# Bullet movement logic will be handled in the main game loop and is defined in player.py file.