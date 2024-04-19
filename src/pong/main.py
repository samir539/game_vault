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
except ImportError:
    print(f"could not load a module")
    sys.exit(2)




#resource handling
def load_image(image_name):
    """
    function to load image from data folder
    :param image_name: the name of the image to load
    :return image: image object
    :return image_rect: object storing rectangular coordinates of the image
    """
    fullname = os.join("data",image_name)
    try: 
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load the wanted image: {fullname}")
        raise SystemExit
    return image, image.get_rect()



#game object classes
class Ball(pygame.sprite.Sprite):
    """
    Class to make instances of the ball object which moves across the screen
    :Methods:
        update: update the state of the ball
        calcnewpos: compute the new position of the ball 
    """
    def __init__(self,vector):
        """
        init method
        :param vector: the start position of the ball
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("ball.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
    
    def update(self):
        newpos = self.calcNewPos(self.rect, self.vector)
        self.rect = newpos


    def calcNewPos(self, rect, vector):
        """
        compute the new position based of the current position of the ball and where it is going 
        """
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)
    

class bat(pygame.sprite.Sprite):
    """
    Class to make instances of the bat object
    :Methods:
        reinit
        update
        moveup
        movedown
    """
    def __init__(self,side):
        pygame.sprite.Sprite.__init__()
        self.image,self.rect = load_image("bat.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = "still"
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0,0]
        #set to center
        if self.side == "left":
            self.rect.midleft = self.area.midleft
        elif self.side == "right":
            self.rect.midright = self.area.midright
    
    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contain(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moveup"

    def movedown(self):
        self.movepos[0] = self.movepos[0] + (self.speed)
        self.state = "movedown"







#game functions




#initalise game




#main loop
