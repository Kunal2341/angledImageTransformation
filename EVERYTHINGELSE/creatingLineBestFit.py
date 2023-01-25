import numpy as np
import matplotlib.pyplot as plt
#Frame 6 and Angle 10 and Height 305 (30.5)
image_f6_a10_h305 = [
    ['0,0', 798, 1689],
    ['0,1', 1632, 1707],
    ['0,2', 2472, 1722],
    ['0,3', 3324, 1740],
    ['1,0', 1077, 1440],
    ['1,1', 1734, 1449],
    ['1,2', 2379, 1455],
    ['1,3', 3063, 1464],
    ['2,0', 1269, 1272],
    ['2,1', 1794, 1284],
    ['2,2', 2328, 1296],
    ['2,3', 2868, 1293],
    ['3,0', 1389, 1173],
    ['3,1', 1830, 1179],
    ['3,2', 2292, 1188],
    ['3,3', 2754, 1182]]
#Frame 26 and Angle 20 and Height 305 (30.5)
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
#Frame 36 and Angle 30 and Height 305 (30.5)
image_f36_a30_h305 = [
    ['0,0', 795, 711],
    ['0,1', 1611, 726],
    ['0,2', 2442, 741],
    ['0,3', 3288, 750],
    ['1,0', 1050, 462],
    ['1,1', 1707, 465],
    ['1,2', 2376, 471],
    ['1,3', 3048, 486],
    ['2,0', 1236, 288],
    ['2,1', 1767, 309],
    ['2,2', 2325, 309],
    ['2,3', 2883, 315],
    ['3,0', 1347, 180],
    ['3,1', 1818, 183],
    ['3,2', 2286, 186],
    ['3,3', 2772, 192]]

def lineOfBestFit(array, print_results=False, imageFile=None):
    """Returns with the slope and y-intercept of the each of the 4 lines of best fit 
    for the given array of points. Lines go from left to right number 0 to 3.
    """
    
    x_points_0 = []
    y_points_0 = []
    x_points_1 = []
    y_points_1 = []
    x_points_2 = []
    y_points_2 = []
    x_points_3 = []
    y_points_3 = []

    for i in array:
        if i[0][2] == '0':
            x_points_0.append(i[1])
            y_points_0.append(i[2])
        elif i[0][2] == '1':
            x_points_1.append(i[1])
            y_points_1.append(i[2])
        elif i[0][2] == '2':
            x_points_2.append(i[1])
            y_points_2.append(i[2])
        elif i[0][2] == '3':
            x_points_3.append(i[1])
            y_points_3.append(i[2])
    x_0 = np.array(x_points_0)
    y_0 = np.array(y_points_0)
    m_0, b_0 = np.polyfit(x_0, y_0, 1)
    
    x_1 = np.array(x_points_1)
    y_1 = np.array(y_points_1)
    m_1, b_1 = np.polyfit(x_1, y_1, 1)
    
    x_2 = np.array(x_points_2)
    y_2 = np.array(y_points_2)
    m_2, b_2 = np.polyfit(x_2, y_2, 1)
    
    x_3 = np.array(x_points_3)
    y_3 = np.array(y_points_3)
    m_3, b_3 = np.polyfit(x_3, y_3, 1)
    
    if imageFile is not None:
        img = cv2.imread(imageFile)
        plt.imshow(image)

    if print_results:
        plt.plot(x_0, y_0, 'o')
        plt.plot(x_0, m_0*x_0 + b_0)
        plt.plot(x_1, y_1, 'o')
        plt.plot(x_1, m_1*x_1 + b_1)
        plt.plot(x_2, y_2, 'o')
        plt.plot(x_2, m_2*x_2 + b_2)
        plt.plot(x_3, y_3, 'o')
        plt.plot(x_3, m_3*x_3 + b_3)
        plt.show()
        
        print("Line for number 1")
        print("y = " + str(m_0) + "x + " + str(b_0))
        print("Line for number 2")
        print("y = " + str(m_1) + "x + " + str(b_1))
        print("Line for number 3")
        print("y = " + str(m_2) + "x + " + str(b_2))
        print("Line for number 4")
        print("y = " + str(m_3) + "x + " + str(b_3))
    
    return [m_0, b_0, m_1, b_1, m_2, b_2, m_3, b_3]
"""
def lineOfBestFit(array):

    # Returns with the slope and y-intercept of the each of the 4 lines of best fit 
    # for the given array of points. Lines go from left to right number 0 to 3.
    #
    
    x_points_0 = []
    y_points_0 = []
    x_points_1 = []
    y_points_1 = []
    x_points_2 = []
    y_points_2 = []
    x_points_3 = []
    y_points_3 = []

    for i in array:
        if i[0][2] == '0':
            x_points_0.append(i[1])
            y_points_0.append(i[2])
        elif i[0][2] == '1':
            x_points_1.append(i[1])
            y_points_1.append(i[2])
        elif i[0][2] == '2':
            x_points_2.append(i[1])
            y_points_2.append(i[2])
        elif i[0][2] == '3':
            x_points_3.append(i[1])
            y_points_3.append(i[2])
    x_0 = np.array(x_points_0)
    y_0 = np.array(y_points_0)
    m_0, b_0 = np.polyfit(x_0, y_0, 1)
    
    x_1 = np.array(x_points_1)
    y_1 = np.array(y_points_1)
    m_1, b_1 = np.polyfit(x_1, y_1, 1)
    
    x_2 = np.array(x_points_2)
    y_2 = np.array(y_points_2)
    m_2, b_2 = np.polyfit(x_2, y_2, 1)
    
    x_3 = np.array(x_points_3)
    y_3 = np.array(y_points_3)
    m_3, b_3 = np.polyfit(x_3, y_3, 1)
    
    
    return x_0, y_0, m_0, b_0, x_1, y_1, m_1, b_1, x_2, y_2, m_2, b_2, x_3, y_3, m_3, b_3
"""
print(lineOfBestFit(image_f26_a20_h305, print_results=True))

"""
y = -0.8755007391191499x + 2385.6612126067766
y = -2.656462585034003x + 6046.918367346919
y = 2.96952942621945x + -5615.853298931099
y = 0.9727155603183576x + -1500.58529096579
w, h = 2160 3840
"""


#for i in image_f26_a20_h305:
# Find the accuracy of the line of best fit - Least Squared Method

# Find the intersection of all 4 line of best fit 

# Graph

#xi = (b_1-b_0) / (m_1-m_0)
#yi = m_0 * xi + b_0

#print(xi, yi)