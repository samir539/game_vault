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
from game_objects.entities import physicalEntity


SCREENWIDTH = 840
SCREENHEIGHT = 520
FPS = 30
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
        # self.cloud,_ = load_image("images/entities/player/idle/00.png")
        # self.cloud_pos = [50,50]
        # self.cloud_move = [False,False]
        # self.cloud.set_colorkey((0,0,0))
        
        
        #assets
        self.player_img, _ = load_image("images/entities/player/idle/00.png")
        self.assets = {"player": self.player_img }
        
        
        #add main player
        self.player_1 = physicalEntity(self, [50,50])
        
        
                
    
    def run_game(self):
        """method to run the game"""
        
        
        movement = [0,0]
        while True:
            self.screen.fill((32,178,170))
            self.clock.tick(FPS)
            
            
        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_d]:
                        if event.key == pygame.K_w:
                            movement = [0,-1]
                        if event.key == pygame.K_s:
                            movement = [0,1]
                        if event.key == pygame.K_a:
                            movement = [-1,0]
                        if event.key == pygame.K_d:
                            movement = [1,0]
            
                # if event.type == pygame.KEYUP:
                #     if event.key in [pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_d]:
                #         if event.key == pygame.K_w:
                #             pass
                #         if event.key == pygame.K_s:
                #             pass
                #         if event.key == pygame.K_a:
                #             pass
                #         if event.key == pygame.K_d:
                #             pass
            self.player_1.update(movement)
            self.player_1.render(self.screen)
            
            
               
            pygame.display.flip()


if __name__ == "__main__":
    Game().run_game()