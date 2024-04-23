import sys
import random 
import math
import os
import getopt
import pygame
import numpy as np
from resource_handling import load_image


SCREENWIDTH = 512
SCREENHEIGHT = 512
cube_dim = pygame.image.load("data/square.png").get_rect()
CUBE_WIDTH = cube_dim.width
CUBE_HEIGHT = cube_dim.height
ORIGIN_X = 0
ORIGIN_Y = 0
DISPLAY = [SCREENWIDTH,SCREENHEIGHT]



class Board():
    def __init__(self):
        self.board_cols_arr = np.linspace((ORIGIN_Y,ORIGIN_Y,ORIGIN_Y,SCREENHEIGHT),(SCREENWIDTH,ORIGIN_Y,SCREENWIDTH,SCREENHEIGHT),CUBE_WIDTH*2,endpoint=False)
        self.board_rows_arr = np.linspace((ORIGIN_X,ORIGIN_X,SCREENHEIGHT,ORIGIN_X),(ORIGIN_X,SCREENHEIGHT,SCREENHEIGHT,SCREENWIDTH),CUBE_HEIGHT*2,endpoint=False)
        
        
        
        
class Food(pygame.sprite.Sprite):
    
    #class variable
    peices_of_food = 0
    max_pieces = 4
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, _ = load_image("apple_food.png")
        self.rand_loc = (np.random.randint(SCREENHEIGHT/(CUBE_HEIGHT*2)),np.random.randint(SCREENWIDTH/(CUBE_WIDTH*2)))
        self.rect = (self.rand_loc[0]*SCREENHEIGHT/(CUBE_HEIGHT*2),self.rand_loc[1]*SCREENWIDTH/(CUBE_WIDTH*2))
        

        


    

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
    
    def extend_snake(self):
        """
        method to extend the snake
        """


if __name__ == "__main__":
    board = Board()
    print(SCREENWIDTH/(CUBE_WIDTH*2))
    print(SCREENHEIGHT/(CUBE_HEIGHT*2))
    print(board.rand_locs)
    



