# Laser tag

We will start the program design on the Raspbery Pi and then if it works well then we will use that but it lags and we need better power control we will use the `nividia jetson`. 
# Things we need to do
- Install the libaries on raspery pi
- List out the specs for the camera
	- Aspect Ratio
	- Video Frame Rate
	- Focal length
- Object Detection (basic)
	- OpenCV
	- TensorFlow
- Object Detection for Humans only
- Distance
	-  Approximate Width and Height of a person
- Be able to get the altiude from the drone data
- Calculate the approximate distance the camera can see from the drone
	- Based on the height of the drone and the angle of the camera figure out the 

# Calculation Steps
![drone calculations of image](https://github.com/iVue-Robotics/iVue-Laser-Tag/blob/main/readmeItems/readMe-Images.png?raw=true)

1. Based of the the aspect ratio of the image compress the image to a estimated vertical birds eye view of the image. 
2. Using the straightening of the stretched image a formula will be extracted with different variables detemining the fading of the stretch
3. With the normalized image caluclate the distance between the lasertag point and the center of the human
4. Using a complex alogrithim and the formula from step 2 calulcate the quickest way to move the point controlling `location (x,y) horz`, `angle`, and `altitude vertical`. 
5. Run the previous 4 steps on first, second, and third frame to approximate the estimated position within the next 2 seconds
6. Calculate the time needed to move
8. Move drone to estimated location of person
9. Shoot

# Example video
![3d design ](https://github.com/iVue-Robotics/iVue-Laser-Tag/blob/main/readmeItems/design3Dgif.gif?raw=true)
## Example video
- Video Details
	- Human moving
	- Human staying still
- Alitude details
- Is drone moving or not
- Angle of camera (preferably not changing but both work) with respect to the horizontal surface. 
- Camera details (if you give name I can look these up)
	- Apeture rate
	- Aspect ratio (16:9 or 4:3)
	- Focal Length


# PLAN
Okay so this is going to be our plan, its a draft and feel free to edit it:

## Other
1. Purchase `Nividia Jetson` *Kavin send the request to jacob so he can place the order*
2. Kavin will decide which **servo** and the **camera** we need and talk to atharva and josh abt how to install it on the camera
## Mechanical
1. break apart the laser tag and figure out which language they use to transfer data. for example how will we be able to hack into its chip/data/ can get info of contact or not. 
2. have a basic 3d model that can house the following--> **Chip including heat sink space**, **servo**, **camera and laser tag**, and wire managment for everything. 
3. May need include external battery, talk to jacob of how to get power from drone for chip. 
## Programmers 
1. Basic Obj Detection
2. Distance using online pics
3. Connect laser tag to nvidia
4. Connect Servo to Nvidia
4. Running base program only on chip.


# Q-Ground Control
https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html

# Accessing Videos 

Contact Kunal for Google drive link (*Can't put it on github*)
# Notes (10/11)
purchase camera
shooting laser using nvidia chip
recive w a chest plate
powering a servo using the nvidia chip

be able to fly drone using nviida chip ---> develop air hp
design mounting bracket
	- battery
	- nano
	- camera
	- servo
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

![points of 3 images](https://github.com/iVue-Robotics/iVue-Laser-Tag/blob/main/readmeItems/Figure_1.png?raw=true)

![distored change for surface](https://github.com/iVue-Robotics/iVue-Laser-Tag/blob/main/readmeItems/Figure_2.png?raw=true)


# Homography

![distored change for surface](https://github.com/iVue-Robotics/iVue-Laser-Tag/blob/main/readmeItems/Figure_3.png?raw=true)

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

I have added all my code to 

GitHub but it is all over the place, (kinda) but feel free to look at it. 

![distored change for surface](https://github.com/iVue-Robotics/iVue-Laser-Tag/blob/main/readmeItems/Figure_solved.jpeg?raw=true)


# Authors

Most of credit goes to my math teacher lol



First off, I use dronekit as the library for the simulator and to communicate to the drone via MAVLink (Learn More About MAVLink Here). Installation for dronekit is just a simple pip command ($ pip install dronekit). In addition to dronekit, you will need to install dronekit SITL (software in the loop) for the actual simulation, like so: $ pip install dronekit-sitl. Next, you will need to install pymavlink using $ pip install pymavlink. Then, install the latest version of MAVProxy at MAVProxy Download (the latest version is near the bottom). This will allow you to forge the connection between the simulator we will be setting up with QGC (QGroundControl). This is important because QGC will allow you to see all the drone's movements as you would in real life, thus acting as a valid testing system. If you have not already, you would need to download QGC as well. The following is the link for that: QGroundControl Download.

That should be all the setup you need. The following is how you would actually connect the system together. First, I suggest you include import subprocess (no need to install as it is part of the Python Standard Library) to allow you to execute command line arguments directly within a file rather than opening three command prompts. You would essentially use the following syntax: subprocess.Popen(command, shell=True) while replacing `command` with the command string. Also, you should import dronkekit's connect functionality using the following line of code: from dronekit import connect. Make sure you have QGC open. The first command you would pass is dronekit-sitl copter --home=-35.363261,149.165230,584,353. This creates an instance of a Software In The Loop Simulator that you can test code on. It's worth noting that the coordinates on this command are of some random air strip, but you can use any valid coordinates for testing purposes. Next, you would execute mavproxy.py --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501 --out 127.0.0.1:14550 --out 127.0.0.1:14551. This is essentially us using packet forwarding to send information from our code to QGC and thus the simulator, all in one line of code. The IP addresses above would suffice for any computer as it is just a loopback internet protocol, so no need to change those. Finally, you would create a vehicle instance like so: vehicle = connect('127.0.0.1:14550', wait_ready=True). Note that the commands must be run in this order. 

Following this, after just about 5 seconds tops, you should see the following screen with `Ready to Fly` (ignore the portion of the picture on the right - that is my wallpaper on my external monitor when I took the screenshot). This means that your connection with the drone has been detected and that QGC recognizes your drone. All that's left to do is to use MAVLink to control the drone (see below section).
image.png

Alright, so now we're at the final stages! Before proceeding, you would need to import connect and VehicleMode from dronekit, sleep from time, and mavutil from pymavlink. The following are the lines of code for that (you can indeed remove the part where we imported only connect from dronekit above): 
from dronekit import connect, VehicleMode
from time import sleep
from pymavlink import mavutil

Now that we have the connection setup and libraries imported, you can control the drone. First, you would command the drone to take off using QGC (you can also do this using code, but it is usually more convenient this way during testing - code below if you want to use it though). 

To control the drone, you will need a method that I named sendCommand(). The following is the method's code: 
def sendCommand(velocity_x, velocity_y, velocity_z, duration):
    global vehicle
    msg = vehicle.message_factory.set_position_target_global_int_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, # lat_int - X Position in WGS84 frame in 1e7 * meters
        0, # lon_int - Y Position in WGS84 frame in 1e7 * meters
        0, # alt - Altitude in meters in AMSL altitude(not WGS84 if absolute or relative)
        # altitude above terrain if GLOBAL_TERRAIN_ALT_INT
        velocity_x, # X velocity in NED frame in m/s
        velocity_y, # Y velocity in NED frame in m/s
        velocity_z, # Z velocity in NED frame in m/s
        0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

    for x in range(0, duration):
        vehicle.send_mavlink(msg)
        sleep(0.001)

The take off code is as follows:
def takeOff(altitude = 5):
    while not vehicle.is_armable:
        sleep(0.5)
    vehicle.mode = VehicleMode("STABILIZE")
    vehicle.armed = True
    while not vehicle.armed:
        sleep(0.5)
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.simple_takeOff(altitude)
    while True:
        if vehicle.location.global_relative_frame.alt >= altitude * 0.95:
            break
        sleep(0.5)

In the first code segment, you pass in the velocity in the three dimensions as parameters and give it a duration in milliseconds to continuously send that command to the vehicle. In the second code segment, you pass in the altitude; the default is 5 feet when not passed a parameter. You'll see that the second method waits on certain conditions to be met - those are essentially just conditions that are required to allow the drone to fly (it may take up to 10-15 seconds at the worst, don't be alarmed if it doesn't work immediately). Utilizing these methods should allow you to perform changes/movement on the drone you can see in QGC - thus allowing you to test.

As usual, if you have any questions or come across any issues after reading this textbook I wrote, please let me know! You can email me back or text me at (470)-226-8494 - admittedly, I reply to texts much faster.