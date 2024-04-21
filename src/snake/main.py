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
except ImportError:
    print(f"could not load a module")
    sys.exit(2)



DISPLAY = [500,500]


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