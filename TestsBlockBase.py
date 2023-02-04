import unittest
from Ball import Ball
from Paddle import Paddle


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(10, 6, 1000, 1000)
        self.ball.x = 495
        self.ball.y = 495
        self.block = Paddle(200, 200, 15, 1000, 1000)
        self.block.top = 500


    pass


if __name__ == '__main__':
    unittest.main()