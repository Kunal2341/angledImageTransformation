import time
start_time = time.time()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from math import *
import cv2
import statistics

plotting = True

# Image Paht
frameImage = "./DATA/distanceCalculationsImages1/frame36.png"
image = cv2.imread(frameImage)

height, width, _ = image.shape
# Inputted from the file "pointInImage.ipynb"
image_f36_a30_h305 = [
    ['0,0', 795, 711],
    ['0,1', 1611, 726],
    ['0,2', 2442, 741],
    ['0,3', 3288, 750],
    ['1,0', 1050, 462],
    ['1,1', 1707, 465],
    ['1,2', 2376, 471],
    ['1,3', 3048, 486],
    ['2,0', 1236, 288],
    ['2,1', 1767, 309],
    ['2,2', 2325, 309],
    ['2,3', 2883, 315],
    ['3,0', 1347, 180],
    ['3,1', 1818, 183],
    ['3,2', 2286, 186],
    ['3,3', 2772, 192]]


if plotting:
    plt.imshow(image)
    plt.title("Original Points")
    for i in image_f36_a30_h305:
        plt.scatter(i[1], i[2], color='purple', marker=',', s=6)
        plt.text(i[1]-200, i[2]-50, i[0] + "(" + str(i[1]) + "," + str(i[2]) +")" , fontsize=6)

if plotting:
    plt.show()
print("--- %s seconds ---" % (time.time() - start_time))
