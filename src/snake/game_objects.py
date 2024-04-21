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

if __name__ == "__main__":
    pass




