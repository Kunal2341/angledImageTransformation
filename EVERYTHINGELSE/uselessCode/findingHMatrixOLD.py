"""
Using an online IDE called streamlit to test out all the numbers for the transformation matrix.
Learned that the matrix is the inverse of the vector.
Learned that the selected mates area could be extended to include the whole image which is then perspective transformed.
"""

import streamlit as st
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


frameImage = "./DATA/distanceCalculationsImages1/frame26.png"
st.write("File Selected: {}".format(frameImage))
if not os.path.exists(frameImage):
    st.error("File Doesn't Exist")

image = cv2.imread(frameImage)
height, width, _ = image.shape

st.title("Finding Homography Matrix")
st.write("The image is {} pixels wide and {} pixels high".format(width, height))

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
#st.write(image_f26_a20_h305)

hopefully_hMatrix = 0

#st.write("Dots on the mat are the points collected")

sourceMatsArrayOne = ((image_f26_a20_h305[12][1],image_f26_a20_h305[12][2]),
                       (image_f26_a20_h305[15][1],image_f26_a20_h305[15][2]),
                       (image_f26_a20_h305[3][1],image_f26_a20_h305[3][2]),
                       (image_f26_a20_h305[0][1],image_f26_a20_h305[0][2])) # CORRECT FINALLY
st.write("Source Mat One: {}".format(sourceMatsArrayOne))

st.write("X is the -extended area being collected by an addition of {}".format(hopefully_hMatrix))

sourceMatsArrayOne = ((image_f26_a20_h305[12][1]+hopefully_hMatrix,image_f26_a20_h305[12][2]+hopefully_hMatrix),
                       (image_f26_a20_h305[15][1]+hopefully_hMatrix,image_f26_a20_h305[15][2]+hopefully_hMatrix),
                       (image_f26_a20_h305[3][1]+hopefully_hMatrix,image_f26_a20_h305[3][2]+hopefully_hMatrix),
                       (image_f26_a20_h305[0][1]+hopefully_hMatrix,image_f26_a20_h305[0][2]+hopefully_hMatrix)) # CORRECT FINALLY

souceMatsArraySingleMat = ((image_f26_a20_h305[9][1],image_f26_a20_h305[9][2]),
                            (image_f26_a20_h305[10][1],image_f26_a20_h305[10][2]),
                            (image_f26_a20_h305[6][1],image_f26_a20_h305[6][2]),
                            (image_f26_a20_h305[5][1],image_f26_a20_h305[5][2]))


st.title("Lets begin the a")
firstDiagonal = (abs(1374-1263)**2 + abs(786-681)**2)**0.5
secondDiagonal = (abs(1263-1077)**2 + abs(948-786)**2)**0.5
thirdDiagonal = (abs(1077-810)**2 + abs(1191-948)**2)**0.5
averageRatio = ((firstDiagonal / secondDiagonal) + (secondDiagonal / thirdDiagonal)) / 2
newFourthDiagonal = thirdDiagonal / averageRatio
bottomleftAngle = np.arctan(((1191 - 681) / (1374 - 810)))*180/np.pi
loweredHeight = newFourthDiagonal * (np.sin(bottomleftAngle*180/np.pi))
extendedWidth = (newFourthDiagonal**2 - loweredHeight**2)**0.5

newLowerX = 810 - extendedWidth
newLowerY = 1191 + loweredHeight

#not working
#extendedWidth = 360-(np.sin(180-(bottomleftAngle+90))*180/np.pi) * newFourthDiagonal

st.write("The first diagonal is {} pixels".format(firstDiagonal))
st.write("The second diagonal is {} pixels".format(secondDiagonal))
st.write("The third diagonal is {} pixels".format(thirdDiagonal))
st.write("The average ratio is {}".format(averageRatio))
st.write("The new fourth diagonal is {} pixels".format(newFourthDiagonal))
st.write("The bottom left angle is {}".format(bottomleftAngle))
st.write("The lowered height is {}".format(loweredHeight))
st.write("The extended width is {}".format(extendedWidth))
st.write("New point ({}, {})".format(int(newLowerX), int(newLowerY)))
st.write("-"*100)
"""
hopefully_hMatrix = 400
I would like to assume that this should be working becuase I am doing the same thing but scaling it up
But becuase of a term I would like to call "linear algebra stuff" it doesn't work so I won't question it
sourceMatsArrayOne = ((image_f26_a20_h305[12][1]-hopefully_hMatrix,image_f26_a20_h305[12][2]-hopefully_hMatrix),
                       (image_f26_a20_h305[15][1]+hopefully_hMatrix,image_f26_a20_h305[15][2]-hopefully_hMatrix),
                       (image_f26_a20_h305[3][1]+hopefully_hMatrix,image_f26_a20_h305[3][2]+hopefully_hMatrix),
                       (image_f26_a20_h305[0][1]-hopefully_hMatrix,image_f26_a20_h305[0][2]+hopefully_hMatrix)) # CORRECT FINALLY
"""
st.write("-"*100)



fig, ax = plt.subplots()
plt.imshow(image)
plt.title("Points Correction")
plt.show()

# Points on the mat
plt.scatter(image_f26_a20_h305[12][1],image_f26_a20_h305[12][2], color='red')
plt.scatter(image_f26_a20_h305[15][1],image_f26_a20_h305[15][2], color='blue')
plt.scatter(image_f26_a20_h305[3][1],image_f26_a20_h305[3][2], color='pink')
plt.scatter(image_f26_a20_h305[0][1],image_f26_a20_h305[0][2], color='black')

# Points extended from mat
plt.scatter(image_f26_a20_h305[12][1]+hopefully_hMatrix,image_f26_a20_h305[12][2]+hopefully_hMatrix, color='red', marker='x')
plt.scatter(image_f26_a20_h305[15][1]+hopefully_hMatrix,image_f26_a20_h305[15][2]+hopefully_hMatrix, color='blue', marker='x')
plt.scatter(image_f26_a20_h305[3][1]+hopefully_hMatrix,image_f26_a20_h305[3][2]+hopefully_hMatrix, color='pink', marker='x')
plt.scatter(image_f26_a20_h305[0][1]+hopefully_hMatrix,image_f26_a20_h305[0][2]+hopefully_hMatrix, color='black', marker='x')

# Points on the single mat

plt.scatter(image_f26_a20_h305[9][1],image_f26_a20_h305[9][2], color='red', marker='^')
plt.scatter(image_f26_a20_h305[10][1],image_f26_a20_h305[10][2], color='blue', marker='^')
plt.scatter(image_f26_a20_h305[6][1],image_f26_a20_h305[6][2], color='pink', marker='^')
plt.scatter(image_f26_a20_h305[5][1],image_f26_a20_h305[5][2], color='black', marker='^')


# New points novemeber 10
plt.scatter(1500, 560, color='red', marker='x')
plt.scatter(2560, 560, color='blue', marker='x')
plt.scatter(3476, 1525, color='pink', marker='x')
plt.scatter(363, 1525, color='black', marker='x')

newPointsSomething = ((1500, 560), (2560, 560), (3476, 1525), (363, 1525))

#st.write("-"*100)
"""
Same points from above just shown
plt.scatter(image_f26_a20_h305[12][1]-hopefully_hMatrix,image_f26_a20_h305[12][2]-hopefully_hMatrix, color='red', marker='x')
plt.scatter(image_f26_a20_h305[15][1]+hopefully_hMatrix,image_f26_a20_h305[15][2]-hopefully_hMatrix, color='blue', marker='x')
plt.scatter(image_f26_a20_h305[3][1]+hopefully_hMatrix,image_f26_a20_h305[3][2]+hopefully_hMatrix, color='pink', marker='x')
plt.scatter(image_f26_a20_h305[0][1]-hopefully_hMatrix,image_f26_a20_h305[0][2]+hopefully_hMatrix, color='black', marker='x')
"""
st.write("-"*100)


st.title("Choose your own --> Not working")
st.pyplot(fig)

pickedSurface = np.array(sourceMatsArrayOne)
pickedSurface = np.array(newPointsSomething)
totalImage = np.array(((0,0),(width,0),(width,height),(0,height)))
#totalImage = pickedSurface

aux,b = cv2.findHomography(pickedSurface,totalImage)

st.write("Points on the mat:")
st.write(sourceMatsArrayOne)
st.write("Points on single mat:")
st.write(souceMatsArraySingleMat)

st.write("Aux:")
st.write("|" + "-"*100 + "|")
st.write("|" + "---[{}]------[{}]--------[{}]".format(aux[0][0], aux[0][1], aux[0][2]) +  "--|")
st.write("|" + "---[{}]------[{}]--------[{}]".format(aux[1][0], aux[1][1], aux[1][2]) +  "--|")
st.write("|" + "---[{}]------[{}]--------[{}]".format(aux[2][0], aux[2][1], aux[2][2]) +  "--|")
st.write("|" + "-"*100 + "|")


auxOrginal = [[-6.53957125e+01, -7.23199644e+01,  1.39103605e+05],
            [1.89539430e+00, -1.73239039e+02,  1.15371514e+05],
            [6.43521558e-05, -3.56429016e-02,  1.00000000e+00]]


"""
[[-1.09620297e+02 -4.38481187e+01  2.29873762e+05]
 [ 4.10830033e+00 -2.46498020e+02  1.88657259e+05]
 [ 2.19809511e-04 -2.11789322e-02  1.00000000e+00]

[[-6.53957125e+01 -7.23199644e+01  1.39103605e+05]
 [ 1.89539430e+00 -1.73239039e+02  1.15371514e+05]
 [ 6.43521558e-05 -3.56429016e-02  1.00000000e+00]]


"""

print(aux) 

"""
[[ 3.21400186e+00,  3.55430794e+00, -2.77553638e+03],
 [-9.31529082e-02,  8.51417581e+00, -6.17547890e+02],
 [-3.16271420e-06,  1.75174102e-03,  1.00000000e+00]]
"""

# c = b^-1 * A

#widPlus = 0
#heiPlus = 0
#st.image(image)
"""
y = 500
x = 500
w = 4000
h = 2000
croppedImg = image[y:y+h, x:x+w]
st.image(croppedImg)
"""
image9 = cv2.warpPerspective(image,aux,(width,height))

un_warped = cv2.warpPerspective(image,aux,(width,height), flags=cv2.INTER_LINEAR)

image9 = cv2.resize(image9, [5000, 5000])
st.write(image9.shape)

st.image(image9,use_column_width=True)
st.write(image9.shape)


st.image(un_warped,use_column_width=True)