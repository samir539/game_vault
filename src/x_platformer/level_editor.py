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
from resource_handling.image_load import load_image, load_multiple_images
from game_objects.entities import physicalEntity
from game_objects.tile_map import TileMap





SCREENWIDTH = 840
SCREENHEIGHT = 512
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
        
    
        #assets
        self.assets = {}
        self.player_img, _ = load_image("data/images/entities/player/idle/00.png")
        self.assets["player"] = self.player_img
        self.assets["grass_tiles"] = load_multiple_images("data/images/tiles/grass")
        self.assets["stone_tiles"] = load_multiple_images("data/images/tiles/stone")
        
        # 
        
        #tile object
        self.tile_path = TileMap(self,tile_size=16)
        
        
        #camera attributes
        self.panning = [2,2]
        
        #mouse pos
        self.mouse_pos = [0,0]
        
        
    def run_game(self):
        """method to run the game"""
        
        
        movement = [0,0]
        
        
        while True:
            mousepos = pygame.mouse.get_pos()
            # print(mousepos)
            # print("this is centerx",self.player_1.entity_rect.centerx)
            # self.panning[0] += ( - self.panning[0])  / 5
            # self.panning[1] += (- self.panning[1])  / 5
            self.screen.fill((100,100,100))
            self.clock.tick(FPS)
            # self.panning[0] += 2
            # self.panning[1] += 0            
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_SPACE]:
                        if event.key == pygame.K_w:
                            self.panning[1] -= 4
                        if event.key == pygame.K_s:
                            self.panning[1] += 4
                        if event.key == pygame.K_a:
                            self.panning[0] -= 4
                        if event.key == pygame.K_d :
                            self.panning[0] += 4
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.MOUSEBUTTONDOWN:
                        print("hello world",self.mousepos)
                    
            
                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_d]:
                        pass
                        # self.panning[0], self.panning[1] = 0,0
                        
            
            #collision handling
            
            
            
            #updates and render
            # self.tile_path.render_tiles(self.screen,self.panning)
            
            
               
            pygame.display.flip()


if __name__ == "__main__":
    Game().run_game()