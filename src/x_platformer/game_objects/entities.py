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
        self.collisions = {"top":False,"bottom":False,"right":False, "left":False}
        
        
        
    def update(self,movement=[0,0],jump=None):
        
        if movement[0] == 1 and not self.collisions["right"]:    #x direction (right)
            self.velocity[0] = min(self.max_veloctiy_x, self.velocity[0] + self.acceleration_x)
        elif movement[0] == 1 and self.collisions["right"]:
            self.velocity[0] = 0
        elif movement[0] == -1 and not self.collisions["left"]: #x direction (left)
            self.velocity[0] = max(-self.max_veloctiy_y, (self.velocity[0] - self.acceleration_x))
        elif movement[0] == -1 and self.collisions["left"]:
            self.velocity[0] = 0
        
            

        elif movement == ["stop_0","stop_1"]:
            self.velocity[0] = 0
        
        #always have gravity acting
        if not self.collisions["bottom"]:
            self.velocity[1] = min(self.max_veloctiy_y, self.velocity[1] + self.acceleration_y)
        elif self.collisions["bottom"]:
            self.velocity[1] = 0
        
        if jump:
            self.velocity[1] = -8
            print("jumps")
            
            
        
        # print("this is the velicty",self.velocity)
        
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]            
        
        
    def render(self,surface):
        self.entity_rect = self.game.assets["player"].get_rect()
        surface.blit(self.game.assets["player"],self.pos)
    
    
