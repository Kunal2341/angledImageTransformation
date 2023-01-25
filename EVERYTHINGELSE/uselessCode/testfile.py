import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


frameImage = "./DATA/distanceCalculationsImages1/frame26.png"

image = cv2.imread(frameImage)
height, width, _ = image.shape


image_f26_a20_h305 = [
    ['0,0', 810, 1191], #0
    ['1,0', 1638, 1206], #1
    ['2,0', 2457, 1224], #2
    ['3,0', 3276, 1236], #3
    ['0,1', 1077, 948], #4
    ['1,1', 1713, 960], #5
    ['2,1', 2376, 972], #6
    ['3,1', 3030, 975], #7
    ['0,2', 1263, 786], #8
    ['1,2', 1779, 795], #9
    ['2,2', 2319, 804], #10
    ['3,2', 2850, 807], #11
    ['0,3', 1374, 681], #12 
    ['1,3', 1824, 690], #13
    ['2,3', 2277, 690], #14
    ['3,3', 2745, 696]] #15

firstYAverage = int((image_f26_a20_h305[12][2] + image_f26_a20_h305[13][2] + 
                image_f26_a20_h305[14][2] + image_f26_a20_h305[15][2])/4)
secondYAverage = int((image_f26_a20_h305[8][2] + image_f26_a20_h305[9][2] + 
                image_f26_a20_h305[10][2] + image_f26_a20_h305[11][2])/4)
thirdYAverage = int((image_f26_a20_h305[4][2] + image_f26_a20_h305[5][2] + 
                image_f26_a20_h305[6][2] + image_f26_a20_h305[7][2])/4)
fourthYAverage = int((image_f26_a20_h305[0][2] + image_f26_a20_h305[1][2] + 
                image_f26_a20_h305[2][2] + image_f26_a20_h305[3][2])/4)

print("First Average is {}".format(firstYAverage))
print("Second Average is {}".format(secondYAverage))
print("Third Average is {}".format(thirdYAverage))
print("Fourth Average is {}".format(fourthYAverage))

ratioFirstSecond = firstYAverage / secondYAverage
ratioSecondThird = secondYAverage / thirdYAverage
averageRatio = (ratioFirstSecond + ratioSecondThird) / 2



allYPoints = [firstYAverage, secondYAverage, thirdYAverage, fourthYAverage]
print("All Y Points are {}".format(allYPoints))

while(allYPoints[-1] < height):
    currentRatios = []
    for i in range(len(allYPoints)-1):
        currentRatios.append(allYPoints[i] / allYPoints[i+1])
    print("Current Ratios are {}".format(currentRatios))
    newPoint = allYPoints[-1] / (sum(currentRatios)/ len(currentRatios))
    print("New Point is {}".format(newPoint))
    allYPoints.append(int(newPoint))

print(allYPoints)