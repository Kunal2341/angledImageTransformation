"""
This was another way to calculate the points in the grid to 
double makesure <copied from buildingTheGrid.py streamlit code>

Only finds the single point outside on known lines. 
"""
print("Angles dont work")
def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
m_2 = 2.9768879001359347
b_2 = -6094.769002595436
middlePointX = 2060.3924627805654
middlePointY = 34.388553077987844


exactPointX = image_f26_a20_h305[2][1]
hypo = get_distance(middlePointX, middlePointY, image_f26_a20_h305[2][1], 
                    image_f26_a20_h305[2][1]*m_2 + b_2)
opp = image_f26_a20_h305[2][1] - middlePointX

print("Hypotenuse: {}".format(hypo))
print("Opposite: {}".format(opp))
angle = np.arcsin(opp/hypo)*180/np.pi
print("Angle: {}".format(angle))
angle2 = np.arcsin(opp/hypo)
print("Angle2: {}".format(angle2))
print("-"*20)


m_3 = 1.0100323310252939
b_3 = -2076.5986928830052
middlePointX = 2060.3924627805654
middlePointY = 34.388553077987844

exactPointX = image_f26_a20_h305[3][1]
hypo = get_distance(middlePointX, middlePointY, image_f26_a20_h305[3][1], 
                    image_f26_a20_h305[3][1]*m_3 + b_3)
opp = image_f26_a20_h305[3][1] - middlePointX

print("Hypotenuse: {}".format(hypo))
print("Opposite: {}".format(opp))
angle = np.arcsin(opp/hypo)*180/np.pi
print("Angle: {}".format(angle))
angle2 = np.arcsin(opp/hypo)
print("Angle2: {}".format(angle2))
print("-"*20)


#---------------------------------------------------------------------------------
# USING TRIG TO FIND THE CLOSE POINTS
def findRightPoints(imagesArray):
    firstDiagonal = (abs(imagesArray[15][1]-imagesArray[11][1])**2 + abs(imagesArray[15][2] -imagesArray[11][2])**2)**0.5
    secondDiagonal = (abs(imagesArray[11][1]-imagesArray[7][1] )**2 + abs(imagesArray[11][2] -imagesArray[7][2] )**2)**0.5
    thirdDiagonal = (abs(imagesArray[7][1]-imagesArray[3][1])**2 + abs(imagesArray[7][2] -imagesArray[3][2])**2)**0.5
    averageRatio = ((firstDiagonal / secondDiagonal) + 
                    (secondDiagonal / thirdDiagonal)) / 2
    newBottomFourthDiagonal = thirdDiagonal / averageRatio
    bottomRightAngle = np.arctan((imagesArray[3][2] - imagesArray[15][2] )/(imagesArray[3][1] - imagesArray[15][1]))*180/np.pi
    loweredHeightBottom = newBottomFourthDiagonal * np.sin(bottomRightAngle*np.pi/180)#*
    extendedWidthBottom = (newBottomFourthDiagonal**2 - loweredHeightBottom**2)**0.5

    newLowerX = imagesArray[3][1] + extendedWidthBottom
    newLowerY = imagesArray[3][2] + loweredHeightBottom

    newZeroDiagonalTop = firstDiagonal * averageRatio

    st.write(newZeroDiagonalTop)
    st.write(bottomRightAngle)
    topExtendedHeight = newZeroDiagonalTop * abs(np.sin(bottomRightAngle*180/np.pi))
    topExtendedWidth = (newZeroDiagonalTop**2 - topExtendedHeight**2)**0.5

    newHigherX = imagesArray[15][1] - topExtendedWidth
    newHigherY = imagesArray[15][2] - topExtendedHeight
    return newLowerX, newLowerY, newHigherX, newHigherY
#lowerRightX, lowerRightY, higherRightX, higherRightY = findRightPoints(image_f26_a20_h305)
def findLeftPoints(imagesArray):
    firstDiagonal = (abs(imagesArray[12][1]-imagesArray[8][1])**2 + abs(imagesArray[8][2]-imagesArray[12][2])**2)**0.5
    secondDiagonal = (abs(imagesArray[8][1]-imagesArray[4][1])**2 + abs(imagesArray[4][2]-imagesArray[8][2])**2)**0.5
    thirdDiagonal = (abs(imagesArray[4][1]-imagesArray[0][1])**2 + abs(imagesArray[0][2]-imagesArray[4][2])**2)**0.5
    averageRatio = ((firstDiagonal / secondDiagonal) + 
                    (secondDiagonal / thirdDiagonal)) / 2
    newFourthDiagonalBottom = thirdDiagonal / averageRatio
    bottomleftAngle = np.arctan(((imagesArray[0][2] - imagesArray[12][2]) / (imagesArray[12][1] - imagesArray[0][1])))*180/np.pi
    bottomloweredHeight = newFourthDiagonalBottom * (np.sin(bottomleftAngle*180/np.pi))
    bottomextendedWidth = (newFourthDiagonalBottom**2 - bottomloweredHeight**2)**0.5

    newLowerX = imagesArray[0][1] - bottomextendedWidth
    newLowerY = imagesArray[0][2] + bottomloweredHeight

    newZeroDiagonalTop = firstDiagonal * averageRatio
    topExtendedHeight = newZeroDiagonalTop * (np.sin(bottomleftAngle*180/np.pi))
    topExtendedWidth = (newZeroDiagonalTop**2 - topExtendedHeight**2)**0.5

    newHigherX = imagesArray[12][1] + topExtendedWidth
    newHigherY = imagesArray[12][2] - topExtendedHeight
    return newLowerX, newLowerY, newHigherX, newHigherY
#lowerLeftX, lowerLeftY, higherLeftX, higherLeftY = findLeftPoints(image_f26_a20_h305)
# New points novemeber 10
#plt.scatter(higherLeftX, higherLeftY, color='red', marker='x')
#plt.scatter(higherRightX, higherRightY, color='blue', marker='x')
#plt.scatter(lowerRightX, lowerRightY, color='pink', marker='x')
#plt.scatter(lowerLeftX, lowerLeftY, color='black', marker='x')


#print("-"*100)
#print(higherLeftX, higherLeftY, higherRightX, higherRightY)
#print(lowerLeftX, lowerLeftY, lowerRightX, lowerRightY)
#---------------------------------------------------------------------------------
