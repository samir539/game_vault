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
from resource_handling.image_load import load_image 


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
        
        #load cloud
        self.cloud,_ = load_image("images/clouds/cloud_1.png")
        self.cloud_pos = [50,50]
        self.cloud_move = [False,False]
                
    
    def run_game(self):
        """method to run the game"""
        while True:
            self.clock.tick(FPS)
            print("this is cloud move bool",self.cloud_move)
            self.cloud_pos[1] += (self.cloud_move[1] - self.cloud_move[0])*5
            self.screen.blit(self.cloud,self.cloud_pos) 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_d]:
                        if event.key == pygame.K_w:
                            self.cloud_move[0] = True
                        if event.key == pygame.K_s:
                            self.cloud_move[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        print("THIS HAPPENED")
                        self.cloud_move[0] = False
                    if event.key == pygame.K_s:
                        self.cloud_move[1] = False
                
        
            
               
            pygame.display.flip()


if __name__ == "__main__":
    Game().run_game()