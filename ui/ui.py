# ui.py
import pygame
import os
from pygame import mixer

pygame.init()
mixer.init()

FONT_LARGE = pygame.font.Font(None, 72)
FONT_MED = pygame.font.Font(None, 40)
FONT_SMALL = pygame.font.Font(None, 30)

HIGHSCORE_FILE = "highscore.txt"


# ---------------------------------------
# LOAD HIGH SCORE
# ---------------------------------------
def read_high_score():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read().strip())
    except:
        return 0


# ---------------------------------------
# SAVE HIGH SCORE
# ---------------------------------------
def write_high_score(score):
    try:
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(score))
    except:
        pass


# -------------------------------------------------
# LEVEL TRANSITION SCREEN  (Score ≥ 500)
# -------------------------------------------------
def show_level_transition(screen, level, duration_ms=1800):
    text = FONT_LARGE.render(f"LEVEL {level}", True, (255, 255, 255))

    start = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start < duration_ms:
        screen.fill((0, 0, 0))
        screen.blit(text, (300, 260))
        pygame.display.update()


# -------------------------------------------------
# GAME OVER SCREEN
# -------------------------------------------------
def game_over_screen(screen, score):
    high = read_high_score()

    # update high score
    if score > high:
        write_high_score(score)
        high = score

    # UI text
    over_text = FONT_LARGE.render("GAME OVER", True, (255, 255, 255))
    score_text = FONT_MED.render(f"Your Score: {score}", True, (255, 255, 255))
    high_text = FONT_MED.render(f"High Score: {high}", True, (255, 255, 255))
    retry_text = FONT_SMALL.render("Press Y to Play Again", True, (255, 255, 255))
    quit_text = FONT_SMALL.render("Press N to Exit", True, (255, 255, 255))

    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        screen.blit(over_text, (240, 160))
        screen.blit(score_text, (270, 260))
        screen.blit(high_text, (270, 310))
        screen.blit(retry_text, (260, 380))
        screen.blit(quit_text, (300, 420))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                if event.key == pygame.K_n:
                    return False
