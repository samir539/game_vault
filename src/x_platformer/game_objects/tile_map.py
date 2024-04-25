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
        self.tilemap = {}
        self.offtile = []
        
        for i in range(3):
            self.tilemap[f"{i},5"] = {"tile_type":"grass", "tile_edition":3,"pos":[i,5]}
    
    def render_tiles(self,surface):
        for i in self.tilemap.values():
            print(i)
        #image comes from self.game.assets()
        #sureface.blit(image, pos)
        # surface.blit(se)
        
        
        
# print(TileMap(5,5).tilemap)
TileMap(5,5).render_tiles(6) 
        
        