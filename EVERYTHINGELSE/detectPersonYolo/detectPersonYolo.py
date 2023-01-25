import cv2
import numpy as np
import time
import sys
import os



# the neural network configuration
config_path = '/Users/kunal/Documents/iVueIntern/yoloFiles/yolov3.cfg'
weights_path = '/Users/kunal/Documents/iVueIntern/yoloFiles/yolov3.weights'
names = '/Users/kunal/Documents/iVueIntern/yoloFiles/coco.names'

if not os.path.exists(config_path) or not os.path.exists(weights_path) or not os.path.exists(names):
    print("error: file not found")
    sys.exit(1)

path_name = "./DATA/vid24TestImages/frame5.png"

if not os.path.exists(path_name):
    print("error: file not found")
    sys.exit(1)

CONFIDENCE = 0.5
SCORE_THRESHOLD = 0.5
IOU_THRESHOLD = 0.5
# loading all the class labels (objects)
labels = open(names).read().strip().split("\n")
# generating colors for each object for later plotting
#colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

image = cv2.imread(path_name)
file_name = os.path.basename(path_name)
filename, ext = file_name.split(".")
h, w = image.shape[:2]
# create 4D blob
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
#print("Image Shape:", image.shape)
print("Blob Shape:", blob.shape)


net.setInput(blob)

ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

start = time.perf_counter()
layer_outputs = net.forward(ln)
time_took = time.perf_counter() - start
print(f"Time took: {time_took:.2f}s")

font_scale = 1
thickness = 1
boxes, confidences, class_ids = [], [], []
for output in layer_outputs:
    # loop over each of the object detections
    for detection in output:
        # extract the class id (label) and confidence (as a probability) of
        # the current object detection
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        # discard out weak predictions by ensuring the detected
        # probability is greater than the minimum probability
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
print(detection.shape)
for i in range(len(boxes)):
    x, y = boxes[i][0], boxes[i][1]
    w, h = boxes[i][2], boxes[i][3]
    text = f"{labels[class_ids[i]]}: {confidences[i]:.2f}"
    print(text)
print("Detected {} objects".format(len(boxes)))
