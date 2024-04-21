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
    from socket import *
    from pygame.locals import *
    import numpy as np
    from game_objects import Snake, Board
    from resource_handling import load_image
except ImportError:
    print(f"could not load a module")
    sys.exit(2)



DISPLAY = [512,512]
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
    # grid_cords = np.
    line_color = (255, 0, 0)
    pygame.draw.line(screen, line_color, (80, 0), (80, 500))
    pygame.draw.line(screen, line_color, (160, 0), (160, 500))

    pygame.display.flip()

    #init snake
    snake = Snake()
    snake_sprites = pygame.sprite.RenderPlain(snake)

    #event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        screen.blit(background,snake.rect,snake.rect)

        snake_sprites.update()
        snake_sprites.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()