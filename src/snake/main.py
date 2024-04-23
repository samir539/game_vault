VERSION = "0.1"
#Implementation of pong (one player vs the computer)

#load modules
# try: 
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
from game_objects import Snake, Board, Food
from resource_handling import load_image
# except ImportError:
#     print(f"could not load a module")
#     sys.exit(2)


SCREENWIDTH = 512
SCREENHEIGHT = 512
ORIGIN_X = 0
ORIGIN_Y = 0
DISPLAY = [SCREENWIDTH,SCREENHEIGHT]
cube_dim = pygame.image.load("data/square.png").get_rect()
CUBE_WIDTH = cube_dim.width
CUBE_HEIGHT = cube_dim.height




def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("snake")

    #background 
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    #blit background
    screen.blit(background,(0,0))
    pygame.display.flip()

    #grid lines
    line_color = (255, 0, 0)
    

    #init snake
    snake = Snake()
    snake_sprites = pygame.sprite.RenderPlain(snake)

    #init board
    board = Board()

    #init food
    food_group = pygame.sprite.Group()
    for i in range(Food.max_pieces):
        food = Food()
        food_group.add(food)

    #init clock 
    clock = pygame.time.Clock()

    #event loop
    while True:
        
        clock.tick(5)
        if snake.lose == True:
            print("you lost")
            pygame.quit()
            exit()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key in [K_RIGHT, K_LEFT, K_UP, K_DOWN]:
                    snake.move_snake(pygame.key.name(event.key))

        #blits and updates      
        screen.blit(background,snake.rect,snake.rect)
        # for i in range(len(board.food_img_list)):
        #     screen.blit(board.food_img_list[i], board.food_locs[i])
        food_group.update()
        food_group.draw(screen)
        snake_sprites.update()
        snake_sprites.draw(screen)

        
        #render board grid
        for i,j in zip(range(board.board_cols_arr.shape[0]), range(board.board_rows_arr.shape[0])):
                pygame.draw.line(screen, line_color, (board.board_cols_arr[i,0], board.board_cols_arr[i,1]), (board.board_cols_arr[i,2], board.board_cols_arr[i,3]))
                pygame.draw.line(screen, line_color, (board.board_rows_arr[j,0],board.board_rows_arr[j,1]), (board.board_rows_arr[j,2], board.board_rows_arr[j,3]))

                
        pygame.display.flip()

if __name__ == "__main__":
    main()
    