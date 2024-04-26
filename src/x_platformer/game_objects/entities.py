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



class physicalEntity():
    def __init__(self,game,pos):
        self.game = game
        self.pos = list(pos)
        self.velocity = [0,0]     
        self.acceleration_y = 0.7   #gravity
        self.acceleration_x = 0.7
        self.max_veloctiy_x, self.max_veloctiy_y = 4,4
        
        
    def update(self,movement=[0,0]):
        #x direction
        # print("this is movement",movement)
        if movement[0] == 1:
            self.velocity[0] = min(self.max_veloctiy_x, self.velocity[0] + self.acceleration_x)
        elif movement[0] == -1:
            self.velocity[0] = max(-self.max_veloctiy_y, (self.velocity[0] - self.acceleration_x))

        elif movement == [-5,-5]:
            self.velocity[0] = 0
        # #y direction
        # elif movement[1] == 1:
        self.velocity[1] = min(self.max_veloctiy_y, self.velocity[1] + self.acceleration_y)
        
        
          
        # self.velocity[1] = min(self.max_veloctiy_y, self.velocity[1] + self.acceleration_y)
        print("this is the velicty",self.velocity)
        
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]            
            
        # self.velocity = self.velocity + self.acceleration
        # self.moved_pos = min(self.max_veloctiy, )
        # self.moved_pos = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]
        # # print("this is moved pos", self.moved_pos)
        # self.pos[0] += self.moved_pos[0]
        # self.pos[1] += self.moved_pos[1]
        
    def render(self,surface):
        surface.blit(self.game.assets["player"],self.pos)
    
    
