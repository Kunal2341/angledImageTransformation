"""
ORGINAL NOT WORKING

Using an online IDE called streamlit to test out all the numbers for the transformation matrix.
Learned that the matrix is the inverse of the vector.
Learned that the selected mates area could be extended to include the whole image which is then perspective transformed.
"""
print("--------------Running--------------")
import streamlit as st
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import math
from PIL import Image, ImageDraw


frameImage = "./DATA/distanceCalculationsImages1/frame26.png"
st.write("File Selected: {}".format(frameImage))
if not os.path.exists(frameImage):
    st.error("File Doesn't Exist")

image = cv2.imread(frameImage)
height, width, _ = image.shape

st.title("Building the grid")
st.write("The image is {} pixels wide and {} pixels high".format(width, height))

image_f26_a20_h305 = [
    ['0,0', 810, 1191], #0
    ['1,0', 1638, 1206], #1
    ['2,0', 2457, 1224], #2
    ['3,0', 3276, 1236], #3
    ['0,1', 1077, 948], #4
    ['1,1', 1713, 960], #5
    ['2,1', 2376, 972], #6
    ['3,1', 3030, 975], #7
    ['0,2', 1263, 786], #8
    ['1,2', 1779, 795], #9
    ['2,2', 2319, 804], #10
    ['3,2', 2850, 807], #11
    ['0,3', 1374, 681], #12 
    ['1,3', 1824, 690], #13
    ['2,3', 2277, 690], #14
    ['3,3', 2745, 696]] #15

firstYAverage = int((image_f26_a20_h305[12][2] + image_f26_a20_h305[13][2] + 
                image_f26_a20_h305[14][2] + image_f26_a20_h305[15][2])/4)
secondYAverage = int((image_f26_a20_h305[8][2] + image_f26_a20_h305[9][2] + 
                image_f26_a20_h305[10][2] + image_f26_a20_h305[11][2])/4)
thirdYAverage = int((image_f26_a20_h305[4][2] + image_f26_a20_h305[5][2] + 
                image_f26_a20_h305[6][2] + image_f26_a20_h305[7][2])/4)
fourthYAverage = int((image_f26_a20_h305[0][2] + image_f26_a20_h305[1][2] + 
                image_f26_a20_h305[2][2] + image_f26_a20_h305[3][2])/4)

st.write("First Average is {}".format(firstYAverage))
st.write("Second Average is {}".format(secondYAverage))
st.write("Third Average is {}".format(thirdYAverage))
st.write("Fourth Average is {}".format(fourthYAverage))

ratioFirstSecond = firstYAverage / secondYAverage
ratioSecondThird = secondYAverage / thirdYAverage
averageRatio = (ratioFirstSecond + ratioSecondThird) / 2

allYPointsCalculated = []
allYPoints = [firstYAverage, secondYAverage, thirdYAverage, fourthYAverage]
while(allYPoints[-1] < height):
    currentRatios = []
    for i in range(len(allYPoints)-1):
        currentRatios.append(allYPoints[i] / allYPoints[i+1])
    newPoint = allYPoints[-1] / (sum(currentRatios)/ len(currentRatios))
    allYPoints.append(int(newPoint))
allYPointsCalculated.extend(allYPoints)

allYPointsReversed = [fourthYAverage, thirdYAverage, secondYAverage, firstYAverage]
while(allYPointsReversed[-1] > 0):
    currentRatios = []
    for i in range(len(allYPointsReversed)-1):
        currentRatios.append(allYPointsReversed[i] / allYPointsReversed[i+1])
    newPoint = allYPointsReversed[-1] / (sum(currentRatios)/ len(currentRatios))
    allYPointsReversed.append(int(newPoint))
allYPointsCalculated.extend(allYPointsReversed)

#----------------------------------------------------------------------
allYPointsCalculatedSet = sorted(set(allYPointsCalculated))
#print(allYPointsCalculatedSet)
horzLinesExtracted = []
for ct in range(len(allYPointsCalculatedSet)-1):
    if allYPointsCalculatedSet[ct+1] - allYPointsCalculatedSet[ct] > 10:
        horzLinesExtracted.append(allYPointsCalculatedSet[ct])        

#print("--"* 20 )
#print(horzLinesExtracted)

horzLinesExtracted = [56, 68, 83, 101, 123, 149, 181, 219, 265, 321, 389, 471, 570, 689, 798, 963, 1214, 1465, 1768, 2133, 2574]
print(len(horzLinesExtracted))
knownYValuesMat = [689, 798, 963, 1214]
def findLineOfBestFit(array):
    x_points_0 = [i[0] for i in array]
    y_points_0 = [i[1] for i in array]
    x_0 = np.array(x_points_0)
    y_0 = np.array(y_points_0)
    m_0, b_0 = np.polyfit(x_0, y_0, 1)
    return m_0, b_0

#----------------------------------------------------------------------------
# LEFT SIDE
changeForFirst = image_f26_a20_h305[13][1]-image_f26_a20_h305[12][1]
changeForSecond = image_f26_a20_h305[9][1]-image_f26_a20_h305[8][1]
changeForThird = image_f26_a20_h305[5][1]-image_f26_a20_h305[4][1]
changeForFourth = image_f26_a20_h305[1][1]-image_f26_a20_h305[0][1]

#print("Change for first is {}".format(changeForFirst))
#print("Change for second is {}".format(changeForSecond))
#print("Change for third is {}".format(changeForThird))
#print("Change for fourth is {}".format(changeForFourth))

changeArray = [changeForFirst, changeForSecond, changeForThird, changeForFourth]
knownMatPoints = [np.array([image_f26_a20_h305[13][1], image_f26_a20_h305[9][1], image_f26_a20_h305[5][1], image_f26_a20_h305[1][1]]), 
                np.array([image_f26_a20_h305[12][1], image_f26_a20_h305[8][1], image_f26_a20_h305[4][1], image_f26_a20_h305[0][1]])]

cuttOffValue = 0 - 2000
timesRan = 0
while True:
    tempNewArray = np.subtract(knownMatPoints[-1], np.array(changeArray))
    #print(tempNewArray)
    if (tempNewArray[0] < cuttOffValue or tempNewArray[1] < cuttOffValue or 
        tempNewArray[2] < cuttOffValue or tempNewArray[3] < cuttOffValue):
        break
    else:
        knownMatPoints.append(tempNewArray)
        timesRan += 1
print("Times Ran is {}".format(timesRan))
print("Len Known Mat Points is {}".format(len(knownMatPoints)))

groupedMatPoints = []
for i in range(len(knownMatPoints)):
    groupedMatPoints.append([[knownMatPoints[i][0], knownYValuesMat[0]],
                        [knownMatPoints[i][1], knownYValuesMat[1]],
                        [knownMatPoints[i][2], knownYValuesMat[2]],
                        [knownMatPoints[i][3], knownYValuesMat[3]]])
#print(groupedMatPoints)
print("Length Grouped Points {}".format(len(groupedMatPoints)))
print("Length Horz Lines {}".format(len(horzLinesExtracted)))
#print(horzLinesExtracted)
newAllPointsLeftSide = []
for i in groupedMatPoints:
    mValue, bValue = findLineOfBestFit(i)
    for yValue in horzLinesExtracted:
        newAllPointsLeftSide.append([int((yValue-bValue)/mValue), yValue])
#print(newAllPointsLeftSide)
print(len(newAllPointsLeftSide))
#---------------------------------------------------------------------------------
# RIGHT SIDE

changeForFirstRight = image_f26_a20_h305[15][1]-image_f26_a20_h305[14][1]
changeForSecondRight = image_f26_a20_h305[11][1]-image_f26_a20_h305[10][1]
changeForThirdRight = image_f26_a20_h305[7][1]-image_f26_a20_h305[6][1]
changeForFourthRight = image_f26_a20_h305[3][1]-image_f26_a20_h305[2][1]

#print("Change for first is {}".format(changeForFirstRight))
#print("Change for second is {}".format(changeForSecondRight))
#print("Change for third is {}".format(changeForThirdRight))
#print("Change for fourth is {}".format(changeForFourthRight))
changeArrayRight = [changeForFirstRight, changeForSecondRight, changeForThirdRight, changeForFourthRight]
knownMatPoints = [np.array([image_f26_a20_h305[14][1], image_f26_a20_h305[10][1], image_f26_a20_h305[6][1], image_f26_a20_h305[2][1]]), 
                np.array([image_f26_a20_h305[15][1], image_f26_a20_h305[11][1], image_f26_a20_h305[7][1], image_f26_a20_h305[3][1]])]
cuttOffValueRight = width + 2000
#-------------------------------------------------------------------------
timesRan = 0
while True:
    tempNewArray = np.add(knownMatPoints[-1], np.array(changeArrayRight))
    #print(tempNewArray)
    if (tempNewArray[0] > cuttOffValueRight or tempNewArray[1] > cuttOffValueRight or 
        tempNewArray[2] > cuttOffValueRight or tempNewArray[3] > cuttOffValueRight):
        break
    else:
        knownMatPoints.append(tempNewArray)
        timesRan += 1
print("Times Ran is {}".format(timesRan))
groupedMatPointsRight = []
for i in range(len(knownMatPoints)):
    groupedMatPointsRight.append([[knownMatPoints[i][0], knownYValuesMat[0]],
                            [knownMatPoints[i][1], knownYValuesMat[1]],
                            [knownMatPoints[i][2], knownYValuesMat[2]],
                            [knownMatPoints[i][3], knownYValuesMat[3]]])

#print(groupedMatPointsRight)

newAllPointsRightSide = []
for i in groupedMatPointsRight:
    mValue, bValue = findLineOfBestFit(i)
    for yValue in horzLinesExtracted:
        newAllPointsRightSide.append([int((yValue-bValue)/mValue), yValue])

print("Lenght rightPoints is {}".format(len(newAllPointsRightSide)))


#print(len(newAllPointsRightSide))
#print(len(newAllPointsLeftSide))
allPointsGridTotal = newAllPointsLeftSide + newAllPointsRightSide
#print(len(allPointsGridTotal))
#print(allPointsGridTotal)
#st.write(allPointsGridTotal)

#print("--"* 20 )


fig, ax = plt.subplots()
plt.imshow(image)
plt.title("Points Correction")

for i in image_f26_a20_h305:
    plt.scatter(i[1], i[2], color='purple', marker=',', s=6)
    plt.text(i[1]-200, i[2]-50, i[0] + "(" + str(i[1]) + "," + str(i[2]) +")" , fontsize=6)

# Points on the mat
plt.scatter(image_f26_a20_h305[12][1],image_f26_a20_h305[12][2], color='red')
plt.scatter(image_f26_a20_h305[15][1],image_f26_a20_h305[15][2], color='blue')
plt.scatter(image_f26_a20_h305[3][1],image_f26_a20_h305[3][2], color='pink')
plt.scatter(image_f26_a20_h305[0][1],image_f26_a20_h305[0][2], color='black')

sourceMatsArrayOne = ((image_f26_a20_h305[12][1],image_f26_a20_h305[12][2]),
                       (image_f26_a20_h305[15][1],image_f26_a20_h305[15][2]),
                       (image_f26_a20_h305[3][1],image_f26_a20_h305[3][2]),
                       (image_f26_a20_h305[0][1],image_f26_a20_h305[0][2])) # CORRECT FINALLY

souceMatsArraySingleMat = ((image_f26_a20_h305[9][1],image_f26_a20_h305[9][2]),
                            (image_f26_a20_h305[10][1],image_f26_a20_h305[10][2]),
                            (image_f26_a20_h305[6][1],image_f26_a20_h305[6][2]),
                            (image_f26_a20_h305[5][1],image_f26_a20_h305[5][2]))


st.title("Conversion Working")
st.pyplot(fig)


#---------------------------------------------------------------------------------
# Single Grid Out
singleGridOut = np.array(((allPointsGridTotal[54][0], allPointsGridTotal[54][1]), 
                          (allPointsGridTotal[159][0], allPointsGridTotal[159][1]),
                          (allPointsGridTotal[164][0], allPointsGridTotal[164][1]), 
                          (allPointsGridTotal[59][0], allPointsGridTotal[59][1])))
# Double Grid Out
doubleGridOut = np.array(((allPointsGridTotal[74][0], allPointsGridTotal[74][1]), 
                          (allPointsGridTotal[179][0], allPointsGridTotal[179][1]),
                          (allPointsGridTotal[186][0], allPointsGridTotal[186][1]), 
                          (allPointsGridTotal[81][0], allPointsGridTotal[81][1])))
# Triple Grid Out
tripleGridOut = np.array(((allPointsGridTotal[94][0], allPointsGridTotal[94][1]), 
                          (allPointsGridTotal[199][0], allPointsGridTotal[199][1]),
                          (allPointsGridTotal[187][0], allPointsGridTotal[187][1]), 
                          (allPointsGridTotal[103][0], allPointsGridTotal[103][1])))

option = st.selectbox('Number of grid outside known', ('Pick One', '1', '2', '3'))
if option == '1':
    pickedSurface = singleGridOut
elif option == '2':
    pickedSurface = doubleGridOut
elif option == '3':
    pickedSurface = tripleGridOut
else:
    pickedSurface = np.array(sourceMatsArrayOne)

totalImage = np.array(((0,0),(width,0),(width,height),(0,height)))
aux,b = cv2.findHomography(pickedSurface,totalImage)

st.sidebar.subheader("Homography Matrix Aux  -{}".format(option))
st.sidebar.write(aux)
st.sidebar.subheader("Homography Matrix B")
st.sidebar.write(b)
#st.write("Aux:")
#st.write("|" + "-"*100 + "|")
#st.write("|" + "---[{}]------[{}]--------[{}]".format(aux[0][0], aux[0][1], aux[0][2]) +  "--|")
#st.write("|" + "---[{}]------[{}]--------[{}]".format(aux[1][0], aux[1][1], aux[1][2]) +  "--|")
#st.write("|" + "---[{}]------[{}]--------[{}]".format(aux[2][0], aux[2][1], aux[2][2]) +  "--|")
#st.write("|" + "-"*100 + "|")


imageResulted = cv2.warpPerspective(image,aux,(width,height))
imageResulted = cv2.resize(imageResulted, [3000, 3000])
st.image(imageResulted,use_column_width=True)
st.write(imageResulted.shape)

#---------------------------------------------------------------------------------
st.header("ALL Image Resulted")
aux1,b1 = cv2.findHomography(singleGridOut,totalImage)
aux2,b2 = cv2.findHomography(doubleGridOut,totalImage)
aux3,b3 = cv2.findHomography(tripleGridOut,totalImage)
singleImg = cv2.warpPerspective(image,aux1,(width,height))
doubleImg = cv2.warpPerspective(image,aux2,(width,height))
tripleImg = cv2.warpPerspective(image,aux3,(width,height))
singleImgResized = cv2.resize(singleImg, [3000, 3000])
doubleImgResized = cv2.resize(doubleImg, [3000, 3000])
tripleImgResized = cv2.resize(tripleImg, [3000, 3000])



img1 = Image.open(frameImage)
drw1 = ImageDraw.Draw(img1, 'RGBA')
drw1.polygon([tuple(i) for i in singleGridOut], (255, 0, 0, 125))
del drw1
img2 = Image.open(frameImage)
drw2 = ImageDraw.Draw(img2, 'RGBA')
drw2.polygon([tuple(i) for i in doubleGridOut], (255, 0, 0, 125))
del drw2
img3 = Image.open(frameImage)
drw3 = ImageDraw.Draw(img3, 'RGBA')
drw3.polygon([tuple(i) for i in tripleGridOut], (255, 0, 0, 125))
del drw3

col1_A, col2_A = st.columns(2)
col1_B, col2_B = st.columns(2)
col1_C, col2_C = st.columns(2)

col1_A.image(img1, caption='Highlighted Area')
col1_B.image(img2, caption='Highlighted Area')
col1_C.image(img3, caption='Highlighted Area')

col2_A.image(singleImgResized, caption='Single Grid')
col2_B.image(doubleImgResized, caption='Double Grid')
col2_C.image(tripleImgResized, caption='Triple Grid')


print("---------------Ended---------------")