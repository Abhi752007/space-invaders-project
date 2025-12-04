import math


class collision:    
    

    def is_collision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
        return distance < 27

