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
# from .. resource_handling.image_load import load_image

class TileMap():
    def __init__(self,game,tile_size):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offtile = []
        
        for i in range(1,10):
            self.tilemap[f"{i},10"] = {"tile_type":"grass_tiles", "tile_edition":2,"pos":[i,15]}
    
    def render_tiles(self,surface):
        for i in self.tilemap.values():
            tile = self.game.assets[i["tile_type"]][i["tile_edition"]]
            pos_x = i["pos"][0]*self.tile_size
            pos_y = i["pos"][1]*self.tile_size
            surface.blit(tile, (pos_x,pos_y))
        
    
if __name__ == "__main__":
    pass
        
        