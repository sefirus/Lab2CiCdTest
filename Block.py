from random import randrange as rnd
import Game
from BlockBase import BlockBase


class Block(BlockBase):

    def __init__(self, poz_x: int, poz_y: int, rows: int, cols: int):
        block_height = 50
        block_width = (Game.SCREEN_WIDTH - cols * 20) / cols
        super().__init__(10 + (block_width + 20) * poz_x, 10 + (block_height + 20) * poz_y, block_width, block_height)
        self.color = (rnd(30, 156), rnd(30, 256), rnd(30, 156))

    pass
