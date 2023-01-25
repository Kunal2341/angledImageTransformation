import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


frameImage = "./DATA/distanceCalculationsImages1/frame26.png"
image = cv2.imread(frameImage)
height, width, _ = image.shape

image_f26_a20_h305 = [
    ['0,0', 810, 1191],
    ['0,1', 1638, 1206],
    ['0,2', 2457, 1224],
    ['0,3', 3276, 1236],
    ['1,0', 1077, 948],
    ['1,1', 1713, 960],
    ['1,2', 2376, 972],
    ['1,3', 3030, 975],
    ['2,0', 1263, 786],
    ['2,1', 1779, 795],
    ['2,2', 2319, 804],
    ['2,3', 2850, 807],
    ['3,0', 1374, 681],
    ['3,1', 1824, 690],
    ['3,2', 2277, 690],
    ['3,3', 2745, 696]] 

sourceMatsArrayOne = ((image_f26_a20_h305[12][1],image_f26_a20_h305[12][2]),
                       (image_f26_a20_h305[15][1],image_f26_a20_h305[15][2]),
                       (image_f26_a20_h305[3][1],image_f26_a20_h305[3][2]),
                       (image_f26_a20_h305[0][1],image_f26_a20_h305[0][2])) # CORRECT FINALLY
"""
Looks like no difference 
sourceMatsArrayOne = ((image_f26_a20_h305[15][1],image_f26_a20_h305[15][2]),
                       (image_f26_a20_h305[12][1],image_f26_a20_h305[12][2]),
                       (image_f26_a20_h305[0][1],image_f26_a20_h305[0][2]),
                       (image_f26_a20_h305[3][1],image_f26_a20_h305[3][2])) #  yes
"""
print(sourceMatsArrayOne)
"""
Top Left
Top Right
Bottom Right
Bottom Left
((1374, 681), (2745, 696), (3276, 1236), (810, 1191))
"""
plt.scatter(1374, 681, color='red')
plt.scatter(2745, 696, color='blue')
plt.scatter(3276, 1236, color='green')
plt.scatter(810, 1191, color='orange')
plt.imshow(image)
plt.title("Points Correction")
plt.show()


print(width, height)

print("The percent of the entire image that the top line holds.")
print(str(sourceMatsArrayOne[1][0]) + "-" + str(sourceMatsArrayOne[0][0]) + "/" + str(width))
print(((sourceMatsArrayOne[1][0]-sourceMatsArrayOne[0][0])/width+1))

print((width/(sourceMatsArrayOne[1][0]-sourceMatsArrayOne[0][0]))*width)

print((height/(sourceMatsArrayOne[2][1]-sourceMatsArrayOne[1][1]))*height)


pickedSurface = np.array(((0,0),(width,0),(width,height),(0,height)))

totalImage = np.array(((0,0),(10755,0),(10755,8640),(0,8640)))


aux,b = cv2.findHomography(pickedSurface,totalImage)

image9 = cv2.warpPerspective(image,aux,(width,height))

plt.imshow(image9)
plt.title("Distortion Correction")
plt.show()



