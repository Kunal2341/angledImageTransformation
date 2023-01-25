"""
Using from https://stackoverflow.com/questions/22656698/perspective-correction-in-opencv-using-python
Building on aspectRatioEditImg.py 

https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
https://stackoverflow.com/questions/38285229/calculating-aspect-ratio-of-perspective-transform-destination-image
https://www.microsoft.com/en-us/research/uploads/prod/2016/11/Digital-Signal-Processing.pdf

I really have no idea whats happening here.
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np

frameImage = "./distanceCalculationsImages1/frame26.png"
im = cv2.imread(frameImage)
w, h = im.shape[0], im.shape[1]
print("w, h: ", w, h)
"""
def unwarp(img, src, dst, testing):
    h, w = img.shape[:2]
    # use cv2.getPerspectiveTransform() to get M, the transform matrix, and Minv, the inverse
    M = cv2.getPerspectiveTransform(src, dst)
    # use cv2.warpPerspective() to warp your image to a top-down view
    warped = cv2.warpPerspective(img, M, (w, h), flags=cv2.INTER_LINEAR)

    if testing:
        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
        f.subplots_adjust(hspace=.2, wspace=.05)
        ax1.imshow(img)
        x = [src[0][0], src[2][0], src[3][0], src[1][0], src[0][0]]
        y = [src[0][1], src[2][1], src[3][1], src[1][1], src[0][1]]
        ax1.plot(x, y, color='red', alpha=0.4, linewidth=3, solid_capstyle='round', zorder=2)
        ax1.set_ylim([h, 0])
        ax1.set_xlim([0, w])
        ax1.set_title('Original Image', fontsize=30)
        ax2.imshow(cv2.flip(warped, 1))
        ax2.set_title('Unwarped Image', fontsize=30)
        plt.show()
    else:
        return warped, M
# We will first manually select the source points 
# we will select the destination point which will map the source points in
# original image to destination points in unwarped image
src = np.float32([(20,     1),
                  (540,  130),
                  (20,    520),
                  (570,  450)])

dst = np.float32([(600, 0),
                  (0, 0),
                  (600, 531),
                  (0, 531)])

unwarp(im, src, dst, True)

cv2.imsave("so.png", im)
#cv2.waitKey(0)[![enter image description here][1]][1]
#cv2.destroyAllWindows()




other code
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[360,50],[2122,470],[2264, 1616],[328,1820]])

ratio=1.6
cardH=math.sqrt((pts1[2][0]-pts1[1][0])*(pts1[2][0]-pts1[1][0])+(pts1[2][1]-pts1[1][1])*(pts1[2][1]-pts1[1][1]))
cardW=ratio*cardH;
pts2 = np.float32([[pts1[0][0],pts1[0][1]], [pts1[0][0]+cardW, pts1[0][1]], [pts1[0][0]+cardW, pts1[0][1]+cardH], [pts1[0][0], pts1[0][1]+cardH]])

M = cv2.getPerspectiveTransform(pts1,pts2)

offsetSize=500
transformed = np.zeros((int(cardW+offsetSize), int(cardH+offsetSize)), dtype=np.uint8);
dst = cv2.warpPerspective(img, M, transformed.shape)

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
"""