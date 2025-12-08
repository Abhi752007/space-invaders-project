# ui.py
# UI helper module for Space Invaders project (pygame)
# Provides:
#   - show_level_transition(screen, level, duration_ms=1800)
#   - game_over_screen(screen, score, highscore_file="highscore.txt")
#   - read_high_score / write_high_score utility functions
#
# Usage examples (from main.py):
#   import ui
#   ui.show_level_transition(screen, 2)
#   play_again = ui.game_over_screen(screen, scores)
#
# The file expects an 'assets' folder alongside containing:
#   - assets/laser.mp3  (used for level 2 transition)
# If audio is missing, it will continue without crashing.

import pygame
import os
from pygame import mixer
import time
import ui

pygame.font.init()
try:
    mixer.init()
except Exception:
    # mixer might be already initialized or unavailable; ignore silently
    pass

# Default fonts (you can replace with a ttf file if you like)
TITLE_FONT = pygame.font.Font(None, 96)
SUB_FONT = pygame.font.Font(None, 40)
SMALL_FONT = pygame.font.Font(None, 28)

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 230, 80)
RED = (230, 50, 50)
BLACK = (0, 0, 0)

# Highscore file (relative to working directory)
DEFAULT_HIGHSCORE_FILE = "highscore.txt"

def read_high_score(path=DEFAULT_HIGHSCORE_FILE):
    """Return integer high score from file, or 0 if not present."""
    try:
        if os.path.exists(path):
            with open(path, "r") as f:
                val = f.read().strip()
                return int(val) if val != "" else 0
    except Exception:
        pass
    return 0

def write_high_score(value, path=DEFAULT_HIGHSCORE_FILE):
    """Write integer high score to file (overwrites)."""
    try:
        with open(path, "w") as f:
            f.write(str(int(value)))
    except Exception:
        pass

def draw_centered_text(surface, text, font, color, y):
    """Draw text centered horizontally at vertical position y."""
    txt_surf = font.render(text, True, color)
    rect = txt_surf.get_rect(center=(surface.get_width() // 2, y))
    surface.blit(txt_surf, rect)

def show_level_transition(screen, level, duration_ms=1800):
    """
    Animated level-transition overlay.
    - level: integer (1,2,3,..)
    - duration_ms: how long to display the animation in milliseconds

    Special behavior: if level == 2 and assets/laser.mp3 exists, plays that sound once.
    This function blocks for duration_ms while rendering animation and consuming events.
    """
    clock = pygame.time.Clock()
    start = pygame.time.get_ticks()
    w, h = screen.get_size()

    # attempt to load laser sound for level 2
    laser_sound = None
    laser_path = os.path.join("assets", "laser.mp3")
    if level == 2 and os.path.exists(laser_path):
        try:
            laser_sound = mixer.Sound(laser_path)
            laser_sound.play()
        except Exception:
            laser_sound = None

    # Pre-compute strings
    title_text = f"LEVEL {level}"
    subtitle_text = "Get Ready..."

    # Animation: scale up title and fade out
    # We'll scale font size from 40 -> 110 and fade alpha 255 -> 0
    while True:
        now = pygame.time.get_ticks()
        elapsed = now - start
        t = min(1.0, elapsed / duration_ms)  # 0..1

        # background dim (draw translucent rect over the game screen)
        overlay = pygame.Surface((w, h), pygame.SRCALPHA)
        alpha = int(180 * (1 - (t * 0.6)))  # little fade of overlay
        overlay.fill((0, 0, 0, alpha))
        screen.blit(overlay, (0, 0))

        # scale the title font size
        # start size and end size:
        start_size = 36
        end_size = 110
        cur_size = int(start_size + (end_size - start_size) * (1 - (1 - t) ** 2))
        # create dynamic font (caching omitted for simplicity)
        try:
            big_font = pygame.font.Font(None, max(12, cur_size))
        except Exception:
            big_font = TITLE_FONT

        # Fade text
        text_alpha = int(255 * (1 - t))
        if text_alpha < 10 and t >= 0.98:
            # final small moment: draw a tiny "GO" flash
            draw_centered_text(screen, "GO!", SUB_FONT, YELLOW, h // 2)
        else:
            # render title with shadow
            title_surf = big_font.render(title_text, True, WHITE)
            title_rect = title_surf.get_rect(center=(w // 2, h // 2 - 20))
            # shadow
            shadow = big_font.render(title_text, True, (10, 10, 10))
            shadow.set_alpha(max(0, text_alpha - 40))
            shadow_rect = shadow.get_rect(center=(w // 2 + 4, h // 2 - 16))
            screen.blit(shadow, shadow_rect)
            title_surf.set_alpha(text_alpha)
            screen.blit(title_surf, title_rect)

            # subtitle
            sub_surf = SUB_FONT.render(subtitle_text, True, YELLOW)
            sub_rect = sub_surf.get_rect(center=(w // 2, h // 2 + 50))
            sub_surf.set_alpha(max(0, min(255, 255 - int(255 * t))))
            screen.blit(sub_surf, sub_rect)

        pygame.display.update()

        # consume events so OS doesn't mark window "not responding"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If user closes window, exit immediately
                pygame.quit()
                raise SystemExit()

        if elapsed >= duration_ms:
            break

        clock.tick(60)

def game_over_screen(screen, score, highscore_file=DEFAULT_HIGHSCORE_FILE):
    """
    Display a game over screen.
    - Shows final score and high score.
    - If the current score is greater than saved highscore, marks a "NEW HIGH SCORE" and saves it.
    - Asks "Play again? (Y/N)" and returns True if player chose to play again, False if quit.

    This function blocks until player presses Y/N keys or clicks the corresponding buttons.
    """
    clock = pygame.time.Clock()
    w, h = screen.get_size()

    # read high score and compare
    high = read_high_score(highscore_file)
    new_high = False
    if score > high:
        new_high = True
        write_high_score(score, highscore_file)
        high = score

    # Optional: try to play a "game over" sound if you have one at assets/gameover.mp3
    gameover_path = os.path.join("assets", "gameover.mp3")
    if os.path.exists(gameover_path):
        try:
            s = mixer.Sound(gameover_path)
            s.play()
        except Exception:
            pass

    # We'll render a static screen with a soft slide-in for the title and a blinking prompt.
    title = "GAME OVER"
    small_title = f"Score: {score}"
    high_title = f"High Score: {high}"
    prompt = "PLAY AGAIN?  (Y / N)   or Click Buttons"

    # Simple buttons (visual, clickable)
    btn_w, btn_h = 160, 48
    btnY = h // 2 + 120
    btn_play_rect = pygame.Rect(w // 2 - btn_w - 10, btnY, btn_w, btn_h)
    btn_quit_rect = pygame.Rect(w // 2 + 10, btnY, btn_w, btn_h)

    blink_timer = 0
    blink_on = True

    running = True
    while running:
        # draw background dark overlay
        overlay = pygame.Surface((w, h))
        overlay.fill((8, 12, 24))
        overlay.set_alpha(230)
        screen.blit(overlay, (0, 0))

        # Draw title with a small drop shadow
        draw_centered_text(screen, title, TITLE_FONT, WHITE, h // 2 - 140)
        draw_centered_text(screen, small_title, SUB_FONT, YELLOW, h // 2 - 60)
        draw_centered_text(screen, high_title, SUB_FONT, WHITE, h // 2 - 20)

        if new_high:
            # Draw a celebratory banner
            banner_font = pygame.font.Font(None, 34)
            txt = "NEW HIGH SCORE!"
            txt_surf = banner_font.render(txt, True, BLACK)
            bg_rect = pygame.Rect(0, 0, txt_surf.get_width() + 30, txt_surf.get_height() + 12)
            bg_rect.center = (w // 2, h // 2 + 20)
            # yellow banner
            banner = pygame.Surface((bg_rect.width, bg_rect.height))
            banner.fill(YELLOW)
            banner.set_alpha(240)
            screen.blit(banner, (bg_rect.left, bg_rect.top))
            screen.blit(txt_surf, (bg_rect.left + 15, bg_rect.top + 6))

        # Draw buttons
        pygame.draw.rect(screen, (40, 160, 40), btn_play_rect, border_radius=8)
        pygame.draw.rect(screen, (160, 40, 40), btn_quit_rect, border_radius=8)
        play_txt = SMALL_FONT.render("PLAY AGAIN", True, WHITE)
        quit_txt = SMALL_FONT.render("QUIT", True, WHITE)
        screen.blit(play_txt, play_txt.get_rect(center=btn_play_rect.center))
        screen.blit(quit_txt, quit_txt.get_rect(center=btn_quit_rect.center))

        # blinking prompt
        blink_timer += clock.get_time()
        if blink_timer > 500:
            blink_on = not blink_on
            blink_timer = 0
        if blink_on:
            draw_centered_text(screen, prompt, SMALL_FONT, WHITE, h // 2 + 80)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # user closed window: quit
                pygame.quit()
                raise SystemExit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n or event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if btn_play_rect.collidepoint(mx, my):
                    return True
                if btn_quit_rect.collidepoint(mx, my):
                    return False

        clock.tick(30)

def brief_message(screen, text, duration_ms=1200):
    """Utility: show a brief centered message for duration_ms (non-blocking to events)."""
    clock = pygame.time.Clock()
    start = pygame.time.get_ticks()
    w, h = screen.get_size()

    while pygame.time.get_ticks() - start < duration_ms:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit()

        overlay = pygame.Surface((w, h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))
        draw_centered_text(screen, text, SUB_FONT, YELLOW, h // 2)
        pygame.display.update()
        clock.tick(60)
