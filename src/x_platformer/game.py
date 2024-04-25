VERSION = "0.1" 

import sys
import random
import math
import os
import getopt
import pygame
from einops import rearrange
from socket import *
from pygame.locals import *
import numpy as np


SCREENWIDTH = 840
SCREENHEIGHT = 520
FPS = 60
DISPLAY =  [SCREENWIDTH, SCREENHEIGHT]




class Game():
    def __init__(self):
        """init game class"""
        pygame.init()
        pygame.display.set_caption("x_platformer")
        self.screen = pygame.display.set_mode(DISPLAY)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.screen.blit(self.background,(0,0))
        pygame.display.flip()
                
    
    def run_game(self):
        """method to run the game"""
        while True:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                else:
                    pass
                
            pygame.display.flip()


if __name__ == "__main__":
    Game().run_game()