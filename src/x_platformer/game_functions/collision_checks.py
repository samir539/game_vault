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




def check_side(rect1,rect2):
    """
    given two rectangles determine if there is an intersection and if so in which direction (from the perspective of the first rectangle)
    """
    if rect1.midtop[1] < rect2.midbottom[1]:
        return "top"
    elif rect1.midright[0] > rect2.midleft[0]:
        return "right"
    elif rect1.midleft[0] < rect2.midright[0]:
        return "left"
    elif rect1.midbottom[1] > rect2.midtop[1]:
        return "bottom"
    