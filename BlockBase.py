import pygame
import Ball


class BlockBase(pygame.Rect):

    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)

    def process_collision(self, ball: Ball):
        if not ball.colliderect(self):
            return
        if ball.direction_x > 0:  # the ball is heading ->
            distance_x = ball.right - self.left
        else:  # the ball is heading <-
            distance_x = self.right - ball.left

        if ball.direction_y > 0:  # the ball is heading downwards
            distance_y = ball.bottom - self.top
        else:  # the ball is heading upwards
            distance_y = self.bottom - ball.top

        if abs(distance_x) <= ball.radius and abs(distance_y) <= ball.radius:  # both distances are small
            ball.direction_x, ball.direction_y = -ball.direction_x, -ball.direction_y
        elif distance_x > distance_y:  # horizontal distance a bigger
            ball.direction_y = -ball.direction_y
        elif distance_y > distance_x:  # vertical distance a bigger
            ball.direction_x = -ball.direction_x
    pass
