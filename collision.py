import math


class collision:    

    def __init__(self):
        pass

    def is_collision(self,enemyX,enemyY,bulletX,bulletY):
        distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
        return distance < 35

