import boto3
import time
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor

start_time = time.time()

photo = "./testImgs/x.jpg"
imagePIL=Image.open(photo)
imgWidth, imgHeight = imagePIL.size 
draw = ImageDraw.Draw(imagePIL)  

client=boto3.client('rekognition')

with open(photo, 'rb') as image:
    response = client.detect_labels(Image={'Bytes': image.read()})

numberPeopleDetected = 0
peopleBoundingBoxes = []
print('Detected labels in ' + photo)    
for label in response['Labels']:
    if label['Name'] == "Person":
        #print (label['Name'] + ' : ' + str(label['Confidence']))
        for instance in label['Instances']:
            #print(instance)
            numberPeopleDetected+=1
            box = instance['BoundingBox']
            left = imgWidth * box['Left']
            top = imgHeight * box['Top']
            width = imgWidth * box['Width']
            height = imgHeight * box['Height']

            print('Left: ' + '{0:.0f}'.format(left))
            print('Top: ' + '{0:.0f}'.format(top))
            print('Face Width: ' + "{0:.0f}".format(width))
            print('Face Height: ' + "{0:.0f}".format(height))
            points = (
                (left,top),
                (left + width, top),
                (left + width, top + height),
                (left , top + height),
                (left, top))
            peopleBoundingBoxes.append([width,height])
            
            draw.line(points, fill='#00d400', width=3)
print("Detected {} people".format(numberPeopleDetected))

#for personInstance in peopleBoundingBoxes:
#    personInstance[0]



imagePIL.save("test.jpg")
print("--- %s seconds ---" % (time.time() - start_time))
