import imageio
import os
directory = "./DATA/vid24TestImgsNotMoving/"
images = []
for filename in os.listdir(directory):
    images.append(imageio.imread(directory+ filename))
imageio.mimsave('pathMovement.gif', images)