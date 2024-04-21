import sys
import random 
import math
import os
import getopt
import pygame
from resource_handling import load_image


class Board(pygame.sprite.Sprite):
    pass

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        """
        init snake on screen
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("square.png ")
        self.move_pos = [0,0]

    def update(self):
        newpos = self.rect.move(self.move_pos)
        self.rect = newpos
        pygame.event.pump()

    def move_snake(self,direction=None):
        # self.move_pos[0] += 32
        self.move_pos[0] += 32


if __name__ == "__main__":
    pass




