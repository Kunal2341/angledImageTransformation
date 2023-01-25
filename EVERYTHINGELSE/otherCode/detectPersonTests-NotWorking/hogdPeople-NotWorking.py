import time

start_time = time.time()
import cv2
import imutils
import numpy as np
import argparse
import os 
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

frame =  "./vid24TestImages/frame3.png"

print(os.path.exists(frame))

image = cv2.imread(frame)
image = imutils.resize(image, width = min(800, image.shape[1])) 

for i in range(10):
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(image, winStride = (8,8))
        
    print(bounding_box_cordinates)
    print(weights)

print("--- %s seconds ---" % (time.time() - start_time))
