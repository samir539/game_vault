import sys
import random 
import math
import os
import getopt
import pygame



def load_image(image_path):
    """
    function to load in a png image
    :param: image name
    :return image: the pygame image object
    :return image.get_rect(): image rectangle coordinates
    """
    # full_name = os.path.join(image_path)
    try:
        image = pygame.image.load(image_path)
        if image.get_alpha() is None:
            image.convert()
        else:
            image.convert_alpha()
    except FileNotFoundError:
        print(f"the desired file was not found, at the filepath: {image_path}")
        raise SystemExit
    return image, image.get_rect()


def load_multiple_images(path):
    """
    Function to load all images in a directory into a list
    """
    image_list =  os.listdir(path)
    pg_image_list = []
    for i in image_list:
        pg_img = pygame.image.load(path + "/" +i)
        if pg_img.get_alpha() is None:
            pg_img.convert()
        else:
            pg_img.convert_alpha()
        pg_image_list.append(pg_img)
    return pg_image_list

    
    # image_list = pygame.image.load()
    # pass
    



if __name__ == "__main__":
    # load_multiple_images("../data/images/clouds")
    load_image("../data/images/entities/player/idle/00.png")