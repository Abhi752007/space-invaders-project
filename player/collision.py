import math
import enemy
def iscollision(enemyX, enemyY, bulletX, bulletY):   # Calculate the distance between enemy and player
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2)) #   If distance is less than a certain threshold, return True (collision detected)
    if distance<27:  # Threshold value for collision is 27 because both player and enemy have a size that makes this value appropriate
        return True
    else:
        return False