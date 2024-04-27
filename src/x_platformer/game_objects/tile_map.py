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
from game_functions.collision_checks import check_side

class TileMap():
    """
    tile are assumed to be squares
    """
    def __init__(self,game,tile_size):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offtile = []
        self.surr_dir = [[0,-1],[1,0],[0,1],[-1,0]] #directions of four nearest tiles
        
        for i in range(2,23):
            self.tilemap[f"{i},13"] = {"tile_type":"grass_tiles", "tile_edition":2,"pos":[i,13]}
        for i in range(1,25):
            self.tilemap[f"10,{i}"] = {"tile_type":"stone_tiles", "tile_edition":2,"pos":[10,i]}
    
    def render_tiles(self,surface):
        for i in self.tilemap.values():
            tile = self.game.assets[i["tile_type"]][i["tile_edition"]]
            pos_x = i["pos"][0]*self.tile_size
            pos_y = i["pos"][1]*self.tile_size
            surface.blit(tile, (pos_x,pos_y))
            
            
    def tile_collision_check(self):
        player_pos = self.game.player_1.pos
        player_tile =[int(x/self.tile_size) for x in player_pos]
        surrounding_tiles = [[player_tile[0] + x[0] ,player_tile[1] + x[1]] for x in self.surr_dir]
        
        
        
    
if __name__ == "__main__":
    pass
        
        