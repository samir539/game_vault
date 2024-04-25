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
        self.velocity = [0,10]        
    
    def update(self,movement=[0,0]):
        self.moved_pos = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]
        print("this is moved pos", self.moved_pos)
        self.pos[0] += self.moved_pos[0]
        self.pos[1] += self.moved_pos[1]
        
    def render(self,surface):
        surface.blit(self.game.assets["player"],self.pos)
    
    
