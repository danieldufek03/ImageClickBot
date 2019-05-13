#!/usr/bin/env python
'''

This Program is designed to find and click sequentially named images, this allows
us to create a generally adaptive bot by simply dragging images to the appropriate
folder and renaming them.

'''
import cv2
import numpy as np
# from matplotlib import pyplot as plt
import pyautogui
import random
import time
import os
from lib.imagesearch import *


__author__ = "Daniel Price-Dufek"
__version__ = "1.0.0"
__maintainer__ = "Daniel Price-Dufek"
__email__ = "dpricedu@harris.com"
__status__ = "Development"

# finds images and clicks images in numbered order
def findImages():
    index = 1
    filename = 'images\\' + str(index) + '.png'
    print(filename)
    while(os.path.exists(filename)):
        print(filename)
        searchAndClick(filename)
        filename = 'images\\' + str(index) + '.png'
        index = index + 1

# finds if any of the images are on the screen and returns the filename
def findImagesOR():
    result = multiImageSearch('OR')
    print(str(result))

def main():
    try:
        findImages()
    except KyeboardInterrupt:
        print('Exiting Main Loop')

if __name__ == '__main__':
    main()
