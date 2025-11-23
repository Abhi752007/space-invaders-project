import pygame

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Window")
clock = pygame.time.Clock()
running = True
bg_color = (30, 30, 30)
font = pygame.font.SysFont(None, 48)
text = font.render('Hello, Pygame!', True, (200, 200, 200))
text_rect = text.get_rect(center=(width // 2, height // 2))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)
    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
