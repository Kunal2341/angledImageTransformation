"""
This runs on all objects later working on just a single object - person
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import os


# the neural network configuration
config_path = '/Users/kunal/Documents/iVueIntern/yoloFiles/yolov3.cfg'
weights_path = '/Users/kunal/Documents/iVueIntern/yoloFiles/yolov3.weights'
names = '/Users/kunal/Documents/iVueIntern/yoloFiles/coco.names'
folder = "./DATA/vid24TestImgsNotMoving/"
CONFIDENCE = 0.8
SCORE_THRESHOLD = 0.5
IOU_THRESHOLD = 0.5
# loading all the class labels (objects)
labels = open(names).read().strip().split("\n")
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
dataResulted = []
for imageFileName in os.listdir(folder):
    
    path_name = folder + imageFileName

    image = cv2.imread(path_name)
    file_name = os.path.basename(path_name)
    filename, ext = file_name.split(".")
    h, w = image.shape[:2]
    # create 4D blob
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    print("Name: "+ imageFileName)
    print("Image Shape:", image.shape)
    #print("Blob Shape:", blob.shape)

    net.setInput(blob)

    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    start = time.perf_counter()
    layer_outputs = net.forward(ln)
    time_took = time.perf_counter() - start
    print(f"Time took: {time_took:.2f}s")
    boxes, confidences, class_ids = [], [], []
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > CONFIDENCE:
                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' width and height
                box = detection[:4] * np.array([w, h, w, h])
                (centerX, centerY, width, height) = box.astype("int")
                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    singleFrameObjs = []
    for i in range(len(boxes)):
        x, y = boxes[i][0], boxes[i][1]
        w, h = boxes[i][2], boxes[i][3]
        text = f"{labels[class_ids[i]]}: {confidences[i]:.2f}"
        if labels[class_ids[i]] == "person":
            singleFrameObjs.append([labels[class_ids[i]], x, y, w, h, confidences[i]])
    print("Detected {} objects".format(len(boxes)))
    print("-"*30)
    dataResulted.append(singleFrameObjs)
    
print(dataResulted)

