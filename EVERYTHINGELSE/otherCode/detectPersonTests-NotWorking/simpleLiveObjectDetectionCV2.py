import cv2 as cv
from scipy.spatial import distance
import numpy as np
from collections import OrderedDict
import os
class Tracker:
    def __init__(self, maxLost = 30):           # maxLost: maximum object lost counted when the object is being tracked
        self.nextObjectID = 0                   # ID of next object
        self.objects = OrderedDict()            # stores ID:Locations
        self.lost = OrderedDict()               # stores ID:Lost_count
        
        self.maxLost = maxLost                  # maximum number of frames object was not detected.
        
    def addObject(self, new_object_location):
        self.objects[self.nextObjectID] = new_object_location    # store new object location
        self.lost[self.nextObjectID] = 0                         # initialize frame_counts for when new object is undetected
        
        self.nextObjectID += 1
    
    def removeObject(self, objectID):                          # remove tracker data after object is lost
        del self.objects[objectID]
        del self.lost[objectID]
    
    @staticmethod
    def getLocation(bounding_box):
        xlt, ylt, xrb, yrb = bounding_box
        return (int((xlt + xrb) / 2.0), int((ylt + yrb) / 2.0))
    
    def update(self,  detections):
        
        if len(detections) == 0:   # if no object detected in the frame
            for objectID in self.lost.keys():
                self.lost[objectID] +=1
                if self.lost[objectID] > self.maxLost: self.removeObject(objectID)
            
            return self.objects
        
        new_object_locations = np.zeros((len(detections), 2), dtype="int")     # current object locations
        
        for (i, detection) in enumerate(detections): new_object_locations[i] = self.getLocation(detection)
            
        if len(self.objects)==0:
            for i in range(0, len(detections)): self.addObject(new_object_locations[i])
        else:
            objectIDs = list(self.objects.keys())
            previous_object_locations = np.array(list(self.objects.values()))
            
            D = distance.cdist(previous_object_locations, new_object_locations) # pairwise distance between previous and current
            
            row_idx = D.min(axis=1).argsort()   # (minimum distance of previous from current).sort_as_per_index
            
            cols_idx = D.argmin(axis=1)[row_idx]   # index of minimum distance of previous from current
            
            assignedRows, assignedCols = set(), set()
            
            for (row, col) in zip(row_idx, cols_idx):
                
                if row in assignedRows or col in assignedCols:
                    continue
                
                objectID = objectIDs[row]
                self.objects[objectID] = new_object_locations[col]
                self.lost[objectID] = 0
                
                assignedRows.add(row)
                assignedCols.add(col)
                
            unassignedRows = set(range(0, D.shape[0])).difference(assignedRows)
            unassignedCols = set(range(0, D.shape[1])).difference(assignedCols)
            
            
            if D.shape[0]>=D.shape[1]:
                for row in unassignedRows:
                    objectID = objectIDs[row]
                    self.lost[objectID] += 1
                    
                    if self.lost[objectID] > self.maxLost:
                        self.removeObject(objectID)
                        
            else:
                for col in unassignedCols:
                    self.addObject(new_object_locations[col])
            
        return self.objects
cfg = '/Users/kunal/Documents/AI-19/ObjectDetection/multi-object-tracker-master/yolo_dir/yolov3.cfg'
weights = '/Users/kunal/Documents/AI-19/ObjectDetection/multi-object-tracker-master/yolo_dir/yolov3.weights'
names = '/Users/kunal/Documents/AI-19/ObjectDetection/multi-object-tracker-master/yolo_dir/coco.names'
yolomodel = {"config_path":cfg,
                "model_weights_path":weights,
                "coco_names":names,
                "confidence_threshold": 0.5,
                "threshold":0.3
                }

print(os.path.exists(yolomodel["config_path"]))
print(os.path.exists(yolomodel["model_weights_path"]))
print(os.path.exists(yolomodel["coco_names"]))

net = cv.dnn.readNetFromDarknet(yolomodel["config_path"], yolomodel["model_weights_path"])
labels = open(yolomodel["coco_names"]).read().strip().split("\n")

np.random.seed(12345)
layer_names = net.getLayerNames()
layer_names = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
print(layer_names)

bbox_colors = np.random.randint(0, 255, size=(len(labels), 3))
maxLost = 5   # maximum number of object losts counted when the object is being tracked
tracker = Tracker(maxLost = maxLost)
#video_src = 0
#cap = cv.VideoCapture(video_src)
(H, W) = (None, None)  # input image height and width for the network
writer = None
frameIMG =  cv.imread("./vid24TestImages/frame1SMALL.png")

print(frameIMG.shape)

#(2160, 3840, 3)
blob = cv.dnn.blobFromImage(frameIMG, 1 / 255.0, (416, 416), swapRB=True, crop=False)

print(blob.shape)

net.setInput(blob)
detections_layer = net.forward(layer_names)   # detect objects using object detection model
#print(len(detections_layer[2][0]))
detections_bbox = []     # bounding box for detections

boxes, confidences, classIDs = [], [], []
for out in detections_layer:
    for detection in out:
        scores = detection[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        if confidence > yolomodel['confidence_threshold']:
            box = detection[0:4] * np.array([W, H, W, H])
        #else:
            #print("-")
print(scores)
print(classID)
print(confidence)

print(yolomodel['confidence_threshold'])

"""while(True):
    
    ok, image = cap.read()
    
    if not ok:
        print("Cannot read the video feed.")
        break

#frameIMG = frameIMG.shape[:2]

blob = cv.dnn.blobFromImage(frameIMG, 1 / 255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)
detections_layer = net.forward(layer_names)   # detect objects using object detection model

detections_bbox = []     # bounding box for detections

boxes, confidences, classIDs = [], [], []
for out in detections_layer:
    for detection in out:
        scores = detection[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        
        if confidence > yolomodel['confidence_threshold']:
            print(detection)
            box = detection[0:4] * np.array([W, H, W, H])
            (centerX, centerY, width, height) = box.astype("int")
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))
            
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            classIDs.append(classID)

idxs = cv.dnn.NMSBoxes(boxes, confidences, yolomodel["confidence_threshold"], yolomodel["threshold"])

if len(idxs)>0:
    for i in idxs.flatten():
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])
        detections_bbox.append((x, y, x+w, y+h))
        clr = [int(c) for c in bbox_colors[classIDs[i]]]
        #cv.rectangle(image, (x, y), (x+w, y+h), clr, 2)
        #cv.putText(image, "{}: {:.4f}".format(labels[classIDs[i]], confidences[i]),
        #          (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, clr, 2)
        print("{}: {:.4f}".format(labels[classIDs[i]], confidences[i]))

objects = tracker.update(detections_bbox)           # update tracker based on the newly detected objects

for (objectID, centroid) in objects.items():
    text = "ID {}".format(objectID)
    cv.putText(image, text, (centroid[0] - 10, centroid[1] - 10), cv.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 2)
    cv.circle(image, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
    
cv.imshow("image", image)
cv.namedWindow('image',cv.WINDOW_NORMAL)
if cv.waitKey(1) & 0xFF == ord('q'):
    break
#print("Detected at (x):", centroid[0], " and (y): ", centroid[1])


#if writer is None:
#    fourcc = cv.VideoWriter_fourcc(*'MP4V')
#    writer = cv.VideoWriter("output.mp4", fourcc, 30, (W*2, H*2), True)
#writer.write(image)
#cap.release()
#cv.destroyWindow("image")"""