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
        self.rect = self.rect.move([1,1])
        # self.direction = None
        self.move_pos = [0,0]

    #class function
    # def round_to_size(n,m):
    #     return n + (m - n)%m
    # #n = 13
    # #m = 10 
    


    def update(self):
        # self.move_pos[0],self.move_pos[1] = round(self.move_pos[0],-1), round(self.move_pos[1],-1) 
        newpos = self.rect.move(self.move_pos)
        # self.rect = self.rect.move([1,1])
        self.rect = newpos
        pygame.event.pump()

    def move_snake(self,direction=None):
        self.move_pos = [0,0]
        if direction == "left":
            self.move_pos[0] -= 16
        if direction == "right":
            self.move_pos[0] += 16
        if direction == "up":
            self.move_pos[1] -= 16
        if direction == "down":
            self.move_pos[1] += 16
            
    


if __name__ == "__main__":
    pass




