VERSION = "0.1"
#Implementation of pong (one player vs the computer)

#load modules
try: 
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
    from game_objects import Snake, Board
    from resource_handling import load_image
except ImportError:
    print(f"could not load a module")
    sys.exit(2)


SCREENWIDTH = 512
SCREENHEIGHT = 512
ORIGIN_X = 0
ORIGIN_Y = 0
DISPLAY = [SCREENWIDTH,SCREENHEIGHT]
cube_dim = pygame.image.load("data/square.png").get_rect()
CUBE_WIDTH = cube_dim.width
CUBE_HEIGHT = cube_dim.height
cols_arr = np.linspace((ORIGIN_Y,ORIGIN_Y,ORIGIN_Y,SCREENHEIGHT),(SCREENWIDTH,ORIGIN_Y,SCREENWIDTH,SCREENHEIGHT),CUBE_WIDTH*2)
rows_arr = np.linspace((ORIGIN_X,ORIGIN_X,SCREENHEIGHT,ORIGIN_X),(ORIGIN_X,SCREENHEIGHT,SCREENHEIGHT,SCREENWIDTH),CUBE_HEIGHT*2)




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

    #init clock 
    clock = pygame.time.Clock()

    #event loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    pass
                if event.key == K_DOWN:
                    pass
                if event.key == K_LEFT:
                    pass
                if event.key == K_RIGHT:
                    snake.move_snake()
                    print("hello world")
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
                    snake.move_pos = [0,0]

        for i in range(cols_arr.shape[0]):
            pygame.draw.line(screen, line_color, (cols_arr[i,0], cols_arr[i,1]), (cols_arr[i,2], cols_arr[i,3]))
            pygame.draw.line(screen, line_color, (rows_arr[i,0],rows_arr[i,1]), (rows_arr[i,2], rows_arr[i,3]))
    
        
        screen.blit(background,snake.rect,snake.rect)
        snake_sprites.update()
        snake_sprites.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    