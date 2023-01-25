import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import arange
from scipy.optimize import curve_fit

displayImg = "./DATA/vid24TestImgsNotMoving/frame0.png"


print("-"*20)
# Only has 'person' objects-
#yoloDetections = [[['person', 2762, 147, 253, 462]], [['person', 2862, 180, 346, 786], ['person', 2861, 195, 340, 795]], [['person', 2754, 300, 364, 847], ['person', 2792, 291, 351, 868], ['person', 2741, 315, 371, 884], ['person', 2785, 299, 362, 910]], [['person', 2390, 358, 376, 920], ['person', 2399, 375, 363, 944]], [['person', 2106, 488, 420, 960], ['person', 2160, 490, 429, 954], ['person', 2098, 497, 423, 1015]], [['person', 1474, 502, 499, 1134], ['person', 1484, 554, 488, 1112], ['person', 1489, 596, 488, 1155]]]

# -, x, y, w, h, confidence --> each 1 for each frame
yoloDetections = [[['person', 2762, 147, 253, 462, 0.9947855472564697]], [['person', 2862, 180, 346, 786, 0.988206148147583], ['person', 2861, 195, 340, 795, 0.9963823556900024]], [['person', 2754, 300, 364, 847, 0.9958668947219849], ['person', 2792, 291, 351, 868, 0.9942713379859924], ['person', 2741, 315, 371, 884, 0.9454245567321777], ['person', 2785, 299, 362, 910, 0.8754267692565918]], [['person', 2390, 358, 376, 920, 0.9966223239898682], ['person', 2399, 375, 363, 944, 0.9987322092056274]], [['person', 2106, 488, 420, 960, 0.9993382096290588], ['person', 2160, 490, 429, 954, 0.8786498308181763], ['person', 2098, 497, 423, 1015, 0.9933274984359741]], [['person', 1474, 502, 499, 1134, 0.9977104067802429], ['person', 1484, 554, 488, 1112, 0.999482274055481], ['person', 1489, 596, 488, 1155, 0.81246417760849]]]
height, width = 2160, 3840

print(f"Working with {len(yoloDetections)} frames")
def findOverLap(obj1, obj2):
    if (obj2[1] > obj1[1] and obj2[1] < (obj1[1] + obj1[3]) and 
        obj2[2] > obj1[2] and obj2[2] < (obj1[2] + obj1[4])):
        return ((obj1[1] + obj1[3]) - obj2[1]) * ((obj1[2] + obj1[4]) - obj2[2])
    elif (obj1[1] > obj2[1] and obj1[1] < (obj2[1] + obj2[3]) and 
        obj1[2] > obj2[2] and obj1[2] < (obj2[2] + obj2[4])):
        return ((obj2[1] + obj2[3]) - obj1[1]) * ((obj2[2] + obj2[4]) - obj1[2])
    else:
        return 0
"""
# Needs to sort the array in order to compare in order to distinguish between the two or one people
ct = 1
for frame in yoloDetections:
    print("Frame {}".format(ct))
    if len(frame) > 1:
        print("Detected More than 1 person")
        for ctdetectedObject in range(len(frame)-1):
            print(findOverLap(frame[ctdetectedObject], frame[ctdetectedObject+1]))

            if (abs(frame[ctdetectedObject][1]- frame[ctdetectedObject+1][1]) < width * 0.02 and 
                abs(frame[ctdetectedObject][2]- frame[ctdetectedObject+1][2]) < height * 0.02):
                betterAccuracyPoint = max(frame[ctdetectedObject][5], frame[ctdetectedObject+1][5])
                if not frame[ctdetectedObject][5] == betterAccuracyPoint:
                    yoloDetections.pop(frame[ctdetectedObject])
                    print("Removed {}".format(frame[ctdetectedObject]))
                else:
                    yoloDetections.pop(frame[ctdetectedObject+1])
    #else:
        #print("Detected 1 person")
            
    ct+=1
"""
# -, x, y, w, h
#-----------------------------------------------------
print("-"*20)

def pointsToImg():
    plt.scatter(0,0, color='red', marker='X')
    plt.scatter(0, height, color='red', marker='X')
    plt.scatter(width, 0, color='red', marker='X')
    plt.scatter(width, height, color='red', marker='X')
    plt.gca().invert_yaxis()

onlyMainPerson = []
for frame in yoloDetections:
    onlyMainPerson.append(frame[0])

feetPoints = []
for objectDet in onlyMainPerson:
    feetPoints.append([int(objectDet[1] + (objectDet[3]*0.5)), int(objectDet[2] + (objectDet[4]*0.75))])
print(feetPoints)
x, y = zip(*feetPoints)
#plt.scatter(x, y)


#pointsToImg()
#plt.show()


print("-"*20)


# define the true objective function
def objective(x, a, b, c):
	return a * x + b * x**2 + c
 

# curve fit second degree polynomial
popt, _ = curve_fit(objective, x, y)
a, b, c = popt
print("Formula:")
print('y = %.5f*x + %.5f*x^2 + %.5f' % (a, b, c))
plt.scatter(x, y)

for i in range(len(feetPoints)):
    plt.annotate(str(i+1), (x[i], y[i]))

x_line = arange(0, width, 1)
y_line = objective(x_line, a, b, c)
plt.plot(x_line, y_line, '--', color='red')
pointsToImg()

img = mpimg.imread(displayImg)
plt.imshow(img)

nextX = x[-1] - (x[-2] - x[-1])
nextY = nextX * a + nextX**2 * b + c

nextX2 = x[-1] - (x[-2] - x[-1])*2
nextY2 = nextX2 * a + nextX2**2 * b + c

plt.scatter(nextX, nextY, color='purple', marker='X')
plt.scatter(nextX2, nextY2, color='purple', marker='X')

plt.show()

print("-"*20)
print(f"After 1 second ({nextX}, {int(nextY)})")
print(f"After 2 second ({nextX2}, {int(nextY2)})")
print("-"*20)

"""
print(x_line)
print(y_line)
print(len(y_line))
print(len(x_line))

print(a, b, c)

print(x)
print(y)
"""
# curve fit third degree polynomial not working
"""
def objective(x, a, b, c, d, e, f):
	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f
 
popt, _ = curve_fit(objective, x, y)
a, b, c, d, e, f = popt
plt.scatter(x, y)
x_line = arange(min(x), max(x), 1)
y_line = objective(x_line, a, b, c, d, e, f)
plt.plot(x_line, y_line, '--', color='red')
pointsToImg()
plt.show()
"""