from circle_shape import *
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(x, y):
        super.__init__(x, y, PLAYER_RADIUS)
