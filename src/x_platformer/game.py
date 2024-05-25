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
from resource_handling.image_load import load_image, load_multiple_images
from game_objects.entities import physicalEntity
from game_objects.tile_map import TileMap
import json


SCREENWIDTH = 840
SCREENHEIGHT = 512
FPS = 30
DISPLAY =  [SCREENWIDTH, SCREENHEIGHT]




class Game():
    def __init__(self,level_json):
        """init game class"""
        pygame.init()
        pygame.display.set_caption("x_platformer")
        self.screen = pygame.display.set_mode(DISPLAY)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.screen.blit(self.background,(0,0))
        self.level = level_json
        pygame.display.flip()
        
    
        #assets
        self.assets = {}
        self.player_img, _ = load_image("data/images/entities/player/idle/00.png")
        self.assets["player"] = self.player_img
        self.assets["grass_tiles"] = load_multiple_images("data/images/tiles/grass")
        self.assets["stone_tiles"] = load_multiple_images("data/images/tiles/stone")
        
        #add main player
        self.player_1 = physicalEntity(self, [50,50])
        self.player_move_unit = 1
        
        #tile object
        self.tile_path = TileMap(self,tile_size=16)
        self.tile_path.tilemap = self.level
        
        #camera attributes
        self.panning = [2,2]
        print(self.panning)
        
        
    def run_game(self):
        """method to run the game"""
        
        
        movement = [0,0]
        
        # print("this is panning",self.panning)
        jump = False
        
        while True:
            # print("this is centerx",self.player_1.entity_rect.centerx)
            self.panning[0] += ((self.player_1.pos[0] - self.screen.get_width()/2) - self.panning[0])  / 5
            self.panning[1] += ((self.player_1.pos[1] - self.screen.get_height()/2) - self.panning[1])  / 5
            self.screen.fill((32,178,170))
            self.clock.tick(FPS)
            
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_SPACE]:
                        if event.key == pygame.K_w:
                            movement = [0,-self.player_move_unit]
                        if event.key == pygame.K_s:
                            movement = [0,self.player_move_unit]
                        if event.key == pygame.K_a:
                            movement = [-self.player_move_unit,0]
                        if event.key == pygame.K_d :
                            movement = [self.player_move_unit,0]
                        if event.key == pygame.K_SPACE:
                            jump = True
                           
            
                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_d]:
                        movement = ["stop_0","stop_1"]
                        
            
            #collision handling
            
            
            
            #updates and render
            self.player_1.update(movement, jump)
            jump = False
            self.player_1.render(self.screen,self.panning)
            self.tile_path.get_surr_tiles()
            self.player_1.collision_check(self.tile_path)
            self.tile_path.render_tiles(self.screen,self.panning)
            
            
               
            pygame.display.flip()


if __name__ == "__main__":
    with open('sample.json', 'r') as file:
        data = json.load(file)
    game_x_plat = Game(data)
    game_x_plat.run_game()