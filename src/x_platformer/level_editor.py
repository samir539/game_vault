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
import json





SCREENWIDTH = 840
SCREENHEIGHT = 512
FPS = 30
DISPLAY =  [SCREENWIDTH, SCREENHEIGHT]



class LevelEditor():
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
        self.assets_map = {1: "grass_tiles", 2:"stone_tiles"}
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
        self.num = 2
        self.tile_type = 1
            
        
        while True:
            self.screen.fill((100,100,100))
            self.mousepos = pygame.mouse.get_pos()
            
            
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                
                if event.type == pygame.KEYDOWN:
                    if event.key in range(K_0, K_9):
                        self.num = int(pygame.key.name(event.key))
                    if event.key in [pygame.K_o, pygame.K_p]:
                        if event.key == pygame.K_o:
                            self.tile_type = 1
                        if event.key == pygame.K_p:
                            self.tile_type = 2  
                            print("this is stone",type(self.assets_map[self.tile_type]),self.assets_map[self.tile_type] )
                            # print()
                        
                    if event.key in [pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_SPACE]:
                        if event.key == pygame.K_w:
                            self.panning[1] -= 4
                        if event.key == pygame.K_s:
                            self.panning[1] += 4
                        if event.key == pygame.K_a:
                            self.panning[0] -= 4
                        if event.key == pygame.K_d :
                            self.panning[0] += 4
                        
                print(type(self.num))    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.tile_path.tilemap[f"{pygame.mouse.get_pos()[0]//self.tile_path.tile_size},{pygame.mouse.get_pos()[1]//self.tile_path.tile_size}"] = {"tile_type":self.assets_map[self.tile_type], "tile_edition":self.num,"pos":[pygame.mouse.get_pos()[0]//self.tile_path.tile_size,pygame.mouse.get_pos()[1]//self.tile_path.tile_size]}
                    print(pygame.mouse.get_pos())
                
           
                        
                    
                
                    
                    
            
            
                        
            
            #collision handling
            
            
            
            #updates and render
            # print("this is the tile map", self.tile_path.tilemap)
            self.tile_path.render_tiles(self.screen,self.panning)
            
            
            # print("this is the tilemap",self.tile_path.tilemap)
            pygame.display.flip()

    def save_tilemap_json(self):
        """
        method to save the generated tilemap
        """
        with open("sample.json", "w") as outfile: 
            json.dump(self.tile_path.tilemap, outfile)
        

if __name__ == "__main__":
    level = LevelEditor()
    level.run_game()
    level.save_tilemap_json()
    
    