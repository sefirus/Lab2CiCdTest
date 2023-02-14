from BlockBase import BlockBase


class Paddle(BlockBase):
    """
    Class, representing paddle
    Attributes
    ----------
    width: float
        width of the paddle
    height: float
        height of teh paddle
    speed: float
        number of pixels the panel moves per frame while moving
    """
    def __init__(self, width: int, height: int, speed: float, screen_h: int, screen_w: int):
        """
        Parameters
        ----------
        width: int
            width of the paddle
        height: int
            height of the paddle
        speed: float
            number of pixels the panel moves per frame while moving
        screen_h:
            screen height in pixels
        screen_w: int
            screen width in pixels
        """
        self.width = width
        self.height = height
        self.speed = speed
        super().__init__(screen_w // 2 - width // 2, screen_h - height - 10, width, height)

    pass
