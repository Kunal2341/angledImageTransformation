width, height = 3840, 2160
point1Secondx,point1Secondy = 1130, 1413
point2Second = (537, 1297)
height, width = 2160, 3840

# Need to get point 1 second

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def angle(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)

print(distance(width/2, height/2, point1Secondx, point1Secondy))
print(angle(width/2, height/2, point1Secondx, point1Secondy))