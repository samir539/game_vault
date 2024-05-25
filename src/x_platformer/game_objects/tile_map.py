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
        self.surr_dir = {"top":[0,-1],"right":[1,0],"bottom":[0,1],"left":[-1,0]} #directions of four nearest tiles
        
        
        # for i in range(2,23):
        #     self.tilemap[f"{i},13"] = {"tile_type":"grass_tiles", "tile_edition":2,"pos":[i,13]}
        
        # for i in range(1,25):
        #     self.tilemap[f"10,{i}"] = {"tile_type":"stone_tiles", "tile_edition":2,"pos":[10,i]}
            
        # for i in range(1,25):
        #     self.tilemap[f"2,{i}"] = {"tile_type":"stone_tiles", "tile_edition":2,"pos":[2,i]}
    
    def render_tiles(self,surface,offset=(0,0)):
        for i in self.tilemap.values():
            tile = self.game.assets[i["tile_type"]][i["tile_edition"]]
            pos_x = i["pos"][0]*self.tile_size
            pos_y = i["pos"][1]*self.tile_size
            surface.blit(tile, (pos_x - offset[0],pos_y - offset[1]))
    
    def get_surr_tiles(self):
        """
        function to find the surrounding tile rects about the player
        """    
        # print("this is the tile map",self.tilemap)
        
        #1.) get player tile position
        #2.) get surrounding tile direction:tile_rect  in dictionary
        player_pos = self.game.player_1.pos
        player_tile = [int(x/self.tile_size) for x in player_pos]
        surrounding_tiles = {x:[player_tile[0] + self.surr_dir[x][0], player_tile[1] + self.surr_dir[x][1]] for x in self.surr_dir}
        print("this is the player tile", player_tile,"these are the surrounding tiles",surrounding_tiles)
        surrounding_rects = {}
        for dir,location in surrounding_tiles.items():
            
            tile_str = ",".join(map(str, location))
            # print("this is the locations",tile_str)
            if tile_str in self.tilemap.keys():
                if dir in {"bottom","right"}:
                    surrounding_rects[dir] = pygame.Rect((location[0]*self.tile_size,location[1]*self.tile_size),(self.tile_size,self.tile_size)) 
                elif dir == "left":
                    surrounding_rects[dir] = pygame.Rect((location[0]*self.tile_size+3,location[1]*self.tile_size+3),(self.tile_size,self.tile_size))
                else:
                    surrounding_rects[dir] = pygame.Rect((location[0]*self.tile_size,location[1]*self.tile_size+16),(self.tile_size,self.tile_size))
                    

        return surrounding_rects
        
        
            
    # def tile_collision_check(self):
    #     self.game.player_1.collisions = dict.fromkeys(self.game.player_1.collisions, False) #Set all collision directions to false
    #     player_pos = self.game.player_1.pos
    #     player_tile =[int(x/self.tile_size) for x in player_pos] #get tile where player is
    #     surrounding_tiles = {x:[player_tile[0] + self.surr_dir[x][0] ,player_tile[1] + self.surr_dir[x][1]] for x in self.surr_dir} #dict of four surrounding tiles and dir
    #     print("these are the surounding tiles",surrounding_tiles, "this is the player tile",player_tile)
    #     #loop through surrounding tiles get the rect and check for collision with player_rect
    #     for tile_dir in surrounding_tiles:
    #         # print("this is tile_dir",tile_dir)
    #         tile_str = ",".join(map(str, surrounding_tiles[tile_dir]))
    #         print("this is tile_str",tile_str)
    #         if tile_str in self.tilemap.keys():
    #             tile_information = self.tilemap[tile_str]
    #             tile_img = self.game.assets[tile_information["tile_type"]][tile_information["tile_edition"]]
    #             dir = check_side(self.game.player_1.entity_rect,tile_img.get_rect(),tile_dir)
                
                
    #             print("this is the collision dir",dir)
    #             # dir = check_side(5,5,tile_dir)
    #             for i in dir:
    #                 self.game.player_1.collisions[i] = True
    #         else:
    #             pass
            


        
        
        
    
if __name__ == "__main__":
    pass
        
        