#load modules
import pygame
from pygame.locals import *


#resource handling




#game object classes




#game functions




#initalise game




#main loop
def main():
    #Init screen
    pygame.init()
    screen = pygame.display.set_mode((150,50))
    pygame.display.set_caption("Basic game")

    #background 
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    #text
    font = pygame.font.Font(None,36)
    text = font.render("Hello world",1,(10,10,10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text,textpos)

    #blit to screen
    screen.blit(background, (0,0))
    pygame.display.flip()

    #event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        screen.blit(background,(0,0))
        pygame.display.flip()
        
if __name__ == "__main__":
    main()