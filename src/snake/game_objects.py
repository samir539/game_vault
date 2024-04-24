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
    max_pieces = 3
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, _ = load_image("apple_food.png")
        self.rand_loc = (np.random.randint(SCREENHEIGHT/(CUBE_HEIGHT)),np.random.randint(SCREENWIDTH/(CUBE_WIDTH)))
        self.rect = (self.rand_loc[0]*SCREENHEIGHT/(CUBE_HEIGHT*2),self.rand_loc[1]*SCREENWIDTH/(CUBE_WIDTH*2))
        
        
        
class SnakeSegment(pygame.sprite.Sprite):
    
    def __init__(self,start_point_x, start_point_y):
        """
        init snake on screen
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("square.png ")
        self.rect = self.rect.move([start_point_x,start_point_y]) #start at center
        self.square_size_x = SCREENWIDTH/(CUBE_WIDTH*2)
        self.square_size_y = SCREENHEIGHT/(CUBE_HEIGHT*2)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.move_pos = [0,0]
        self.lose = False
        self.direction = "right"

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

        
class SnakeFull():
    
    def __init__(self, snake_segment_sprite_group,start_len=7):
        """
        method to init full snake where the snake is represented by a list of snake segment sprite objects
        :param snake_segment_head: instance of the SnakeSegment object that serves as the head of the snake
        """
        self.square_size_x = SCREENWIDTH/(CUBE_WIDTH*2)
        self.square_size_y = SCREENHEIGHT/(CUBE_HEIGHT*2)
        self.direction = "right"
        self.sprite_group  = snake_segment_sprite_group
        self.head = list(self.sprite_group)[0]
        self.snake_full_list = []
        self.snake_full_list.append(self.head)
        self.extend(start_len)
        
    def ambulate(self):
        for i in range(len(self.snake_full_list)-1,0,-1):
            self.snake_full_list[i].rect.top, self.snake_full_list[i].rect.left =  self.snake_full_list[i-1].rect.top, self.snake_full_list[i-1].rect.left

    
    def growth_loc(self,direction,x,y):
        if direction == "right":
            x,y = x - self.square_size_x, y
        if direction == "left":
            x,y = x + self.square_size_x, y
        if direction == "up":
            x,y = x , y - self.square_size_y
        if direction == "down":
            x,y = x, y + self.square_size_y
        return x,y 
    
    def extend(self,extention_num):
        for i in range(extention_num):
            x,y = self.snake_full_list[i].rect.left, self.snake_full_list[i].rect.top
            x,y = self.growth_loc(self.direction,x,y)
            ith_seg = SnakeSegment(x,y)
            self.sprite_group.add(ith_seg)
            self.snake_full_list.append(ith_seg)


if __name__ == "__main__":
    board = Board()
    print(SCREENWIDTH/(CUBE_WIDTH*2))
    print(SCREENHEIGHT/(CUBE_HEIGHT*2))
    print(board.rand_locs)
    



