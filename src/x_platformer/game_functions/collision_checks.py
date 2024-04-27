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




def check_side(rect1,rect2,dir=None):
    """
    given two rectangles determine if there is an intersection and if so in which direction (from the perspective of the first rectangle)
    """
    collisions = []
    if dir == "bottom":
        collisions.append("bottom")
    if dir == "right":
        collisions.append("right")
    if dir == "left" :
        collisions.append("left")
    if dir == "top":
        collisions.append("top")
    # if rect1.centerx < rect2.centerx:
    #     return "left"
    # if rect1.midbottom[1] > rect2.midtop[1]:
    #     return "bottom"
    # print("these are the collisions",collisions)
    return collisions
    