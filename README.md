# Angled Image to Top-Down View

This repisitory is a continuation of work I completed at my internship at DronesiVue. Previously the code was designed for an angled drones image as that is where all the math is based from but it is in progress of converting any sort of angled image of a surface to a top down view. 

# Current running 

`streamlit run buildingTheGridBase.py`

This converts an image with already predefinied points that describe a square in the image, working on converting it to just take in the height and angle of the image

# Things we need to do
- Install the libaries on raspery pi
- List out the specs for the camera
	- Aspect Ratio
	- Video Frame Rate
	- Focal length
- Be able to get the altiude from the drone data
- Calculate the approximate distance the camera
	- Based on the height and the angle of the camera 

# Example video
![3d design ](https://github.com/Kunal2341/angledImageTransformation/blob/main/readmeItems/design3Dgif.gif?raw=true)
```
law of sins in order to calculate distance
```
# Stuff
**DJI_0024**
|File|Time (sec)|Altitude|Angle|
|-|-|-|-|
|`frame0.png`|0|7.9|24|
|`frame1.png`|1|7.9|24|
|`frame2.png`|2|7.9|24|
|`frame3.png`|3|7.9|24|
|`frame4.png`|4|7.9|24|
|`frame5.png`|5|7.9|24|

# New data email
Okay so after many thoughts this is what I have decide to figure out the answer to this problem 
`When taking arieal image the real world distance between 2 objects in the image and 2 objects in real life has a gradient as you go futher away from center from all corners, whats the formula/graph/measure of that gradient?`

So in order to solve this I need to so one of 2 things, using the same camera (DJI Mavic Zoom 2) from 1 foot off the ground (someone can hold and not fly) film a printed grid. The grid can be like on piece of paper but it needs to take the entire image. So might need to paste together multiple sheets of paper. 

This can also be done on a tile floor where every measurement periodic tile size is the same. 

The grid should be 1 cm by 1 cm for the most specific data but that is not as forced, just needs to be same for all pieces of paper so I can accuratly count/measure. 

Many data points are prefered like at 1 ft altidue periodic stops at every 10 degrees starting at 80 and up to 30. Every degree above 45 will likely to have the top part of image above ground or extremely far away. 

I would also like to see how the gradient is affected by the altidue so same measurments but at a 2, 4, 6, and possibly 8 and 10 (prefered). 

This can just be a long recorded video as the camera angle is changing and a quick 1 second stop at the the angle interval. 

# Linear Perspective Calculations

![points of 3 images](https://github.com/Kunal2341/angledImageTransformation/blob/main/readmeItems/Figure_1.png?raw=true)

![distored change for surface](https://github.com/Kunal2341/angledImageTransformation/blob/main/readmeItems/Figure_2.png?raw=true)


# Homography

![distored change for surface](https://github.com/Kunal2341/angledImageTransformation/blob/main/readmeItems/Figure_3.png?raw=true)

So looking at this image, I was able to create 4 lines of best fits from each of the 4 arrays of points. I manually picked the point for each corner with an interface I have designed which I can use for the other angles. They are colored left to right [orange, red, purple, and grey]. Since they are all linear lines then using the least squared regression technique, I can judge (based on the overall size of the image and difference in y values) that the r-value is extremely close to 1. It can be in the range from [-1. 1] so it gives good lines. Now to find the intersection point, I have found the average of 

- Line 1 and Line 2
- Line 1 and Line 3
- Line 1 and Line 4
- Line 2 and Line 3
- Line 2 and Line 4
- Line 3 and Line 4

Which gives an (x,y) point (graphed as a star but can't see in this image). 

Now using a function called cv2.findHomography and cv2.warpPerspective which do the following, When I input the 4 corner points of the gym mat, into this function (using linear algebra which I barely understood and my friend explained to me) it returns a transformation matrix. This is a set of 9 numbers-oriented in a 3 by 3 grid which by multiplying it by each x,y coordinate you are able to stretch the image which gives the following resulting image. 
Figure_2.png

Right now it's flipped, but I am still figuring out the order of the 4 points in order to create it normally. 

This transformation matrix will now be used to the entire image to shape it correctly to a birds-eye view. I have been doing lots of research and I found this link which helped me understand it, 

https://learnopencv.com/feature-based-image-alignment-using-opencv-c-python/

Now when I shape the entire image there are going to be part of the image which will be blacked out. in order to have a rectangular image but that won't be as bad. I have also created a YOLO model to detect a person which is working well and using the bounding box on the image multiplied by the same transformation matrix I will be able to accurately locate the person. 
I have found the following code which serves my purpose perfectly but it is in C++, but I need it in python. So right now I am struggling with converting it to python, so if you know someone that that knows both C++ and Python, it will be extremely useful. 

https://scode7.blogspot.com/2019/05/perspective-transformation-opencv-c.html

![distored change for surface](https://github.com/Kunal2341/angledImageTransformation/blob/main/readmeItems/Figure_solved.jpeg?raw=true)


