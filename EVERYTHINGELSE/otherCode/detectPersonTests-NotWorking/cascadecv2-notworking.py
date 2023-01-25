import time
start_time = time.time()

from PIL import Image
import numpy as np
import cv2
import os
pedestrian_cascade = cv2.CascadeClassifier("./haarcascade_fullbody.xml")

frame =  "./vid24TestImages/frame3.png"
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
print(os.path.exists(frame))
PIL_img = Image.open(frame).convert('L') # convert it to grayscale
img_numpy = np.array(PIL_img,'uint8')
#id = int(os.path.split(imagePath)[-1].split(".")[1])

pedestrians = pedestrian_cascade.detectMultiScale(img_numpy, 1.1, 1)

print(pedestrians)

print("--- %s seconds ---" % (time.time() - start_time))
