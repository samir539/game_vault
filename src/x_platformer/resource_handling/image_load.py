import sys
import random 
import math
import os
import getopt
import pygame



def load_image(image):
    """
    function to load in a png image
    :param: image name
    :return image: the pygame image object
    :return image.get_rect(): image rectangle coordinates
    """
    full_name = os.path.join("data",image)
    try:
        image = pygame.image.load(full_name)
        if image.get_alpha() is None:
            image.convert()
        else:
            image.convert_alpha()
    except FileNotFoundError:
        print(f"the desired file was not found, filename: {full_name}")
        raise SystemExit
    return image, image.get_rect()



if __name__ == "__main__":
    pass