# Player module


Playerimage=pygame.image.load('player.png')
playerX=370  # starting coordinates of the plyaer
playerY=480
playerX_change=0  # to change the position of the player

# Player function(position)
def player(x,y):
    screen.blit(Playerimage,(x,y)) # blit means to draw


# Game's Loop

    running=True
    while running:

        # bg color
        screen.fill((0,0,0))

        # Event loop
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        
            # Binding keys with the player movement


            if event.type==pygame.KEYDOWN:   # .KEYDOWN checks if any key is pressed
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:   # .key checks which key is pressed
                    playerX_change -=5   # move left
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    playerX_chang +=5   # move right

                if event.type==pygame.KEY_SPACE:
                    if bullet_state=="ready":   # to ensure only one bullet is fired at a time
                        bulletX=playerX   # get the current x coordinate of the player to fire the bullet from there
                    fire_bullet(playerX,bulletY)
                    playerX=bulletX   # to align the bullet with the player

            if event.type==pygame.KEYUP:   # .KEYUP checks if any key is released
                if event.key==pygame.K_LEFT or event.key==pygame.K_a or event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                        playerX_change=0   # stop moving when key is released

        playerX +=playerX_change   # updating the player's position(x coordinate)
        
        # boundary conditions
        if playerX<=0:
            playerX=0
        elif playerX>=736:   # 736 is the width of the screen - width of the player image(800-64)
            playerX=736

        # Bullet Movement
        if bulletY<=0:
            bulletY=480
            bullet_state="ready"

        if bullet_state=="fire":
            fire_bullet(bulletX,bulletY)
            bulletY -=bulletY_change   # moving the bullet upwards


        player(playerX,playerY)
        pygame.display.update()
