import sys
import random 
import math
import os
import getopt
import pygame
from resource_handling import load_image


SCREENWIDTH = 512
SCREENHEIGHT = 512
cube_dim = pygame.image.load("data/square.png").get_rect()
CUBE_WIDTH = cube_dim.width
CUBE_HEIGHT = cube_dim.height

class Board(pygame.sprite.Sprite):
    pass

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        """
        init snake on screen
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("square.png ")
        self.rect = self.rect.move([1,1])
        self.square_size_x = SCREENWIDTH/(CUBE_WIDTH*2)
        self.square_size_y = SCREENHEIGHT/(CUBE_HEIGHT*2)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.move_pos = [0,0]
        self.lose = False

    def update(self):
        newpos = self.rect.move(self.move_pos)
        if not self.area.contains(newpos):
            self.lose = True
        self.rect = newpos
        pygame.event.pump()

    def move_snake(self,direction=None):
        self.move_pos = [0,0]
        if direction == "left":
            self.move_pos[0] -= self.square_size_x
        if direction == "right":
            self.move_pos[0] += self.square_size_x
        if direction == "up":
            self.move_pos[1] -= self.square_size_y
        if direction == "down":
            self.move_pos[1] += self.square_size_y


if __name__ == "__main__":
    pass




