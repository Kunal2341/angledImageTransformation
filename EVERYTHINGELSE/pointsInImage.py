import cv2
import os
def click_event(event, x, y, flags, params):
    dataSaved = []
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        print("[{},{}],".format(x*3,y*3))
"""
## Video 1 - distanceCalculationsImages1
- frame 0-8 is 10
- frame 9-24 is 10-20
- frame 25-30 is 20
- frame 31-34 is 20-30
- frame 35-44 is 30

## Video 2 - distanceCalculationsImages2
- frame 0-4 is 15
- frame 5-8 is 15-20
- frame 9-12 is 20
- frame 13-16 is 20-25
- frame 17-21 is 25
- frame 22-24 is 25-30
- frame 25-29 is 30
- frame 30-32 is 30-35
- frame 33-37 is 35

## Video 3 - distanceCalculationsImages3
- frame 0-2 is 20
- frame 2-10 is 20-25
- frame 11-13 is 25
- frame 14-16 is 25-30
- frame 17-19 is 30
- frame 20-26 is 30-35
- frame 27-30 is 35
- frame 31-33 is 35-40
- frame 34-39 is 40
- frame 40-46 is 40-45
- frame 47-55 is 45
"""
folderPath1 = "./DATA/distanceCalculationsImages1/"
folderPath2 = "./DATA/distanceCalculationsImages2/"
folderPath3 = "./DATA/distanceCalculationsImages3/"

def printType(frameNum):
    if frameNum >= 0 and frameNum <= 8:
        return 10
    elif frameNum >= 9 and frameNum <= 24:
        return round(((frameNum-9) * (20-10)) / (24-9)) + 10
    elif frameNum >= 25 and frameNum <= 30:
        return 20
    elif frameNum >= 31 and frameNum <= 34:
        return round(((frameNum-31) * (30-20)) / (34-31)) + 20
    elif frameNum >= 35 and frameNum <= 44:
        return 30
    else:
        return 0

choosenFrames_1 = [0,9,12,15,17,19,22,24,27,31,32,33,34,38]
choosenFrames_2 = [0,5,7,8,10,13,14,16,19,22,23,24,28,30,31,32,35]
choosenFrames_3 = [0,2,4,6,9,12,14,15,16,18,20,22,24,26,29,31,33,36,40,42,44,48]


for frameNum in choosenFrames_1:
    print("-"*20)
    frameImage = folderPath+"frame"+str(frameNum)+".png"
    print(frameImage)
    img = cv2.imread(frameImage)
    img = cv2.resize(img, (1280,720)) #Scaled down by 3
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    answer = ""
    print(printType(frameNum))
    print("-"*20)
    while answer != "yes":
        answer = input("Copied, allowed to move on to next?")
        if answer == "break":
            break