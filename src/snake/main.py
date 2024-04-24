VERSION = "0.1"
#Implementation of snake (one player vs the computer)

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
from game_objects import SnakeSegment, SnakeFull, Board, Food
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
    

    #init snake_segment and snake full
    snake = SnakeSegment(SCREENHEIGHT/2, SCREENWIDTH/2)
    snake_sprites = pygame.sprite.Group(snake)
    
    snake_full = SnakeFull(snake_sprites)


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
    list(snake_full.sprite_group)[0].move_snake("right")
    while True:
        screen.fill(0)
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
                    if event.key == K_RIGHT and list(snake_full.sprite_group)[0].direction == "left":
                        pass
                    elif event.key == K_LEFT and list(snake_full.sprite_group)[0].direction == "right":
                        pass
                    elif event.key == K_UP and list(snake_full.sprite_group)[0].direction == "down":
                        pass
                    elif event.key == K_DOWN and list(snake_full.sprite_group)[0].direction == "up":
                        pass
                    else:
                        list(snake_full.sprite_group)[0].move_snake(pygame.key.name(event.key))
                        list(snake_full.sprite_group)[0].direction = pygame.key.name(event.key)

                    
                    

        #blits and updates      
        screen.blit(background,snake.rect,snake.rect)
        snake_full.ambulate()
        #if snake head collides with a sprite in food group
        # extend snake
        # spawn new food
        # remove old food
        
        # if pygame.Rect.colliderect(list(snake_full.sprite_group)[0].rect, food_group):
        #     print("HELLLLOOO")
        
        # if pygame.sprite.spritecollideany(list(snake_full.sprite_group)[0], food_group):
        #     print("helllllllooooooo")
        
        if pygame.sprite.groupcollide(snake_full.sprite_group, food_group,dokilla=False,dokillb=True):
            snake_full.extend(1)
            if len(food_group) < Food.max_pieces:
                food = Food()
                food_group.add(food)
        # print( type(list(snake_full.sprite_group)[0].rect))
        # if pygame.Rect.collidepoint(list(snake_full.sprite_group)[0].rect.center,snake_full.sprite_group ):
        #     snake.lose = True
        # if pygame.sprite.spritecollideany(list(snake_full.sprite_group)[0], snake_full.sprite_group):
        #     snake.lose = True
        if pygame.sprite.spritecollideany(snake_full.head,snake_full.snake_full_list[2:]):
            snake.lose = True
            
        # print("HELLO",type(list(snake_full.sprite_group)[0].rect))
        # print("HELLO",type(list(food_group)[1].rect))
        # if list(snake_full.sprite_group)[0].rect.colliderect(food_group):
        #     print("hello world")
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
    
    