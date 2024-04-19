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
    fullname = os.path.join("data",image_name)
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
    def __init__(self, vector):
        """
        init method
        :param vector: the start position of the ball
        """
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("ball.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0
    
    def update(self):
        angle,z = self.vector
        newpos = self.calcNewPos(self.rect, self.vector)
        self.rect = newpos
        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if (tl and tr) or (bl and br):
                angle = -angle 
            if tl and bl:
                # self.offcourt(player=2)
                angle = math.pi - angle
            if tr and br:
                # self.offcourt(player=1)
                angle = math.pi - angle
        else:
            player1.rect.inflate(-3, -3)
            player2.rect.inflate(-3, -3)
            if self.rect.colliderect(player1.rect) and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            elif self.rect.colliderect(player2.rect) and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
        self.vector = (angle,z)


    def calcNewPos(self, rect, vector):
        """
        compute the new position based of the current position of the ball and where it is going 
        """
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)
    

class Bat(pygame.sprite.Sprite):
    """
    Class to make instances of the bat object
    :Methods:
        reinit
        update
        moveup
        movedown
    """
    def __init__(self,side):
        pygame.sprite.Sprite.__init__(self)
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
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moveup"

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = "movedown"










#game functions




#initalise game




#main loop

def main():
    #screen
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Pong")

    #background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,255))

    #players 
    global player1
    global player2
    player1 = Bat("left")
    player2 = Bat("right")

    #init ball
    speed = 15
    ball = Ball((0.50,speed))

    #sprites
    playersprites = pygame.sprite.RenderPlain((player1, player2))
    ballsprite = pygame.sprite.RenderPlain(ball)

    #blit
    screen.blit(background,(0,0))
    pygame.display.flip()

    #init clock 
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == "QUIT":
                return
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    player1.moveup()
                if event.key == K_z:
                    player1.movedown()
                if event.key == K_UP:
                    player2.moveup()
                if event.key == K_DOWN:
                    player2.movedown()
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_z:
                    player1.movepos = [0,0]
                    player1.state = "still"
                if event.key == K_UP or event.key == K_DOWN:
                    player2.movepos = [0,0]
                    player2.state = "still"
        
        screen.blit(background,ball.rect,ball.rect)
        screen.blit(background,player1.rect, player1.rect)
        screen.blit(background,player2.rect, player2.rect)
        ballsprite.update()
        playersprites.update()
        ballsprite.draw(screen)
        playersprites.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

