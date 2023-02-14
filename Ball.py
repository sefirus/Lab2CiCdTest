import pygame
from random import randrange as rnd


class Ball(pygame.Rect):
    """
    Class, representing flying ball
    Attributes
    ----------
    direction_x: int
        Can be 1(->) or -1(<-). Represents horizontal direction of the ball
    direction_y: int
        Can be 1(v) or -1(^). Represents vertical direction of the ball
    radius: int
        radius of the ball
    speed: float
        number of pixels the block moves along each axis per frame while moving
    box_dimension: float
        diagonal size of ball`s box
    """
    def __init__(self, radius: int, default_speed: int,  screen_h: int, screen_w: int):
        """
        Constructor
        Parameters
        ----------
        radius: int
            radius of the ball
        default_speed: int
            default number of pixels the block moves on each axe per frame while moving
        screen_h:
            screen height in pixels
        screen_w: int
            screen width in pixels
        """
        self.direction_x = 1
        self.direction_y = -1
        self.radius = radius
        self.speed = default_speed
        self.box_dimension = int(radius * 2 ** 0.5)
        super().__init__(rnd(self.box_dimension, screen_h - self.box_dimension), screen_w // 2, self.box_dimension,
                         self.box_dimension)
    pass
