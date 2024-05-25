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
        self.entity_rect = self.game.assets["player"].get_rect()
        
        
    def collision_check(self,tilemap):
        """
        check the collisions of the entity with surrounding tile environment
        :param surr_tiles: dictionary of surrounding tiles pos:dir
        """
        self.collisions = {"top":False,"bottom":False,"right":False, "left":False}
        #get surrounding 4 cubes 
        #check collisions
        #get direction of collisions and set self.collisions
        entity_rect = pygame.Rect((self.pos[0],self.pos[1]),(self.entity_rect.width,self.entity_rect.height))
        # print("this is the pos",self.pos)
        # print("this is the entity_rect",entity_rect)
        
        surr_dict = tilemap.get_surr_tiles()
        print("this is surr-dict",surr_dict)
        for dirs,rects in surr_dict.items():
            print("these are the dirs",dirs)
            # print("this is the entity_rect",entity_rect,rects)
            if pygame.Rect.colliderect(entity_rect,rects):
                print("this happened")
                self.collisions[dirs] = True
        print("these are the collisiosn",self.collisions)
                
                
        
        
        
    def update(self,movement=[0,0],jump=None):
        self.entity_rect = self.game.assets["player"].get_rect()
        if movement[0] == 1 and not self.collisions["right"]:    #x direction (right)
            self.velocity[0] = min(self.max_veloctiy_x, self.velocity[0] + self.acceleration_x)
        elif movement[0] == 1 and self.collisions["right"]:
            self.velocity[0] = 0
        elif movement[0] == -1 and not self.collisions["left"]: #x direction (left)
            self.velocity[0] = max(-self.max_veloctiy_x, (self.velocity[0] - self.acceleration_x))
        elif movement[0] == -1 and self.collisions["left"]:
            self.velocity[0] = 0
        
            

        elif movement == ["stop_0","stop_1"]:
            self.velocity[0] = 0
        
        #always have gravity acting
        if not self.collisions["bottom"]:
            self.velocity[1] = min(self.max_veloctiy_y, self.velocity[1] + self.acceleration_y)
        elif self.collisions["bottom"]:
            self.velocity[1] = 0
            
        if self.collisions["top"]:
            self.velocity[1] = 0
        
        if jump:
            self.velocity[1] = -8
            print("jumps")
            
            
        
        # print("this is the velicty",self.velocity)
        
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]            
        
        
    def render(self,surface, offset):
        self.entity_rect = self.game.assets["player"].get_rect()
        print(offset[0])
        surface.blit(self.game.assets["player"],(self.pos[0] - offset[0],self.pos[1] - offset[1]))
    
    
