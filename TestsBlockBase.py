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

    def test_top_bounce(self):
        self.ball.direction_x = 1
        self.ball.direction_y = 1
        self.block.process_collision(self.ball)
        self.assertEqual(self.ball.direction_y, -1)
        self.assertEqual(self.ball.direction_x, 1)

        self.ball.direction_x = -1
        self.ball.direction_y = 1
        self.block.process_collision(self.ball)
        self.assertEqual(self.ball.direction_y, -1)
        self.assertEqual(self.ball.direction_x, -1)

    def test_bottom_bounce(self):
        self.block.bottom = 500
        self.ball.direction_x = 1
        self.ball.direction_y = -1
        self.block.process_collision(self.ball)
        self.assertEqual(self.ball.direction_y, 1)
        self.assertEqual(self.ball.direction_x, 1)

        self.block.bottom = 500
        self.ball.direction_x = -1
        self.ball.direction_y = -1
        self.block.process_collision(self.ball)
        self.assertEqual(self.ball.direction_y, 1)
        self.assertEqual(self.ball.direction_x, -1)
    pass

    def test_right_bounce(self):
        self.block.top = 400
        self.block.left = 505
        self.ball.direction_x = 1
        self.ball.direction_y = -1
        self.block.process_collision(self.ball)
        self.assertEqual(self.ball.direction_y, -1)
        self.assertEqual(self.ball.direction_x, -1)

        self.ball.direction_x = 1
        self.ball.direction_y = 1
        self.block.process_collision(self.ball)
        self.assertEqual(self.ball.direction_y, 1)
        self.assertEqual(self.ball.direction_x, -1)

    def test_left_bounce(self):

        self.block.top = 400
        self.block.right = 505
        self.ball.direction_x = -1
        self.ball.direction_y = -1
        self.block.process_collision(self.ball)
        self.assertEqual(self.ball.direction_y, -1)
        self.assertEqual(self.ball.direction_x, 1)

        self.ball.direction_x = -1
        self.ball.direction_y = 1
        self.block.process_collision(self.ball)
        self.assertEqual(self.ball.direction_y, 1)
        self.assertEqual(self.ball.direction_x, 1)

    pass


if __name__ == '__main__':
    unittest.main()