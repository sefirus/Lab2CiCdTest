import pygame
import Ball


class BlockBase(pygame.Rect):

    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)

    def process_collision(self, ball: Ball):
        if not ball.colliderect(self):
            return

    pass
