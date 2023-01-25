import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
#from PIL import Image
import math
def extract_image_one_fps(video_source_path, numsec):
    """
    Extracts every *numsec* miliseconds
    1000 = 1 second
    Last frame can't be opened
    """
    vidcap = cv2.VideoCapture(video_source_path)
    count = 0
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*numsec)) # 2 second***   
        success,image = vidcap.read()
        ## Stop when last frame is identified
        image_last = cv2.imread("frame{}.png".format(count-1))
        if np.array_equal(image, image_last):
            break
        cv2.imwrite("frame%d.png" % count, image)     # save frame as PNG file
        print( '{}.sec reading a new frame:{}'.format(count,success))
        count += 1

#video = "/Users/kunal/Documents/iVueIntern/laserTagVideos/DJI_0024.MP4"
#frameExample = "/Users/kunal/Documents/iVueIntern/iVue-Laser-Tag/vid24TestImages/frame0.png"
# Get width and height of image
# Get bounding box for person
# Get center of the person 
#frame1 = Image.open(frameExample)
#print(frame1.size)
#height = 1000 #cm
#angle = 60 #between 0 - 90
#viewingAngleCam = 160
"""
    |\ #Angle A
    | \  
    |  \
    |   \
[h] |    \ [b]
    |     \
    |      \
    |_______\ #Angle C
  #Angle B [d] 
"""
"""
Each square is 2’x2' for a total grid size of 6’x6' with the following specification for each video:

Sensor Height, Angle(s), and Distance for Video 1:
30.5” Sensor Height Above Ground | 10°, 20°, and 30° Gimbal Angles | 9’ From Ground Directly Beneath Sensor To Center of Cone

frame 0-8 is 10
frame 9-24 is 10-20
frame 25-30 is 20
frame 31-34 is 20-30
frame 35-44 is 30

Sensor Height, Angle(s), and Distance for Video 2:
47.5” Sensor Height Above Ground | 35°, 30°, 25°, 20°, and 15° Gimbal Angles | 9’ From Ground Directly Beneath Sensor To Center of Cone

frame 0-4 is 15
frame 5-8 is 15-20
frame 9-12 is 20
frame 13-16 is 20-25
frame 17-21 is 25
frame 22-24 is 25-30
frame 25-29 is 30
frame 30-32 is 30-35
frame 33-37 is 35

Sensor Height, Angle(s), and Distance for Video 3:
64.5” Sensor Height Above Ground | 20°, 25°, 30°, 35°, 40°, and 45° Gimbal Angles |  9’ From Ground Directly Beneath Sensor To Center of Cone

frame 0-2 is 20
frame 2-10 is 20-25
frame 11-13 is 25
frame 14-16 is 25-30
frame 17-19 is 30
frame 20-26 is 30-35
frame 27-30 is 35
frame 31-33 is 35-40
frame 34-39 is 40
frame 40-46 is 40-45
frame 47-55 is 45
"""

print("-"*20)
video = "/Users/kunal/Documents/iVueIntern/laserTagVideos/DISTANCE/DJI_0001.MP4"
#extract_image_one_fps(video, 1000)
frameImage = "./distanceCalculationsImages1/frame26.png"
known_distance_ft = 9 # feet
known_distance_inch = 9 * 12  # inches 
anglefromHorz = 20
height = 30.5 #inches
angleFromVertical = 90 - anglefromHorz
angleOfElevation = 180 - angleFromVertical - 90
calculated_distance = height / math.sin(angleOfElevation) * math.sin(angleFromVertical)
known_hypotenuse = math.sqrt(known_distance_inch**2 + height**2)
calculated_hypotenuse = math.sqrt(calculated_distance**2 + height**2)
print("-"*20)

print("File exists: {}".format(os.path.exists(video)))
print("Angle from vertical: {}".format(angleFromVertical))
print("Angle of elevation: {}".format(angleOfElevation))
print("Calculated Hypotenuse {} inches".format(calculated_hypotenuse))
print("Known Hypotenuse {} inches".format(known_hypotenuse))
print("Calculated Distance: {} inches".format(calculated_distance))
print("Known Distance: {} inches".format(known_distance_inch))
print("-"*20)
#Frame 6 and Angle 10 and Height 305 (30.5)
image_f6_a10_h305 = [
    ['0,0', 798, 1689],
    ['0,1', 1632, 1707],
    ['0,2', 2472, 1722],
    ['0,3', 3324, 1740],
    ['1,0', 1077, 1440],
    ['1,1', 1734, 1449],
    ['1,2', 2379, 1455],
    ['1,3', 3063, 1464],
    ['2,0', 1269, 1272],
    ['2,1', 1794, 1284],
    ['2,2', 2328, 1296],
    ['2,3', 2868, 1293],
    ['3,0', 1389, 1173],
    ['3,1', 1830, 1179],
    ['3,2', 2292, 1188],
    ['3,3', 2754, 1182]]
#Frame 26 and Angle 20 and Height 305 (30.5)
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
#Frame 36 and Angle 30 and Height 305 (30.5)
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


x = []
y = []
for i in image_f6_a10_h305:
    x.append(i[1])
    y.append(i[2])
plt.scatter(x, y)
x = []
y = []
for i in image_f26_a20_h305:
    x.append(i[1])
    y.append(i[2])
plt.scatter(x, y)
x = []
y = []
for i in image_f36_a30_h305:
    x.append(i[1])
    y.append(i[2])
plt.scatter(x, y)
plt.scatter(x, y)
plt.show()