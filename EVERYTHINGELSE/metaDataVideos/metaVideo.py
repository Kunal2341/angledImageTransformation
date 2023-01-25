video = "/Users/kunal/Documents/iVueIntern/laserTagVideos/DJI_0026.MP4"
fileL = "/Users/kunal/Documents/iVueIntern/laserTagVideos/file24.mp4"
#import ffmpeg
#vid = ffmpeg.probe(fileL)
#print(vid['streams'])
#from os.path import exists
#print(exists(video))
#import subprocess
#from tinytag import TinyTag
  
# Pass the filename into the
# Tinytag.get() method and store
# the result in audio variable
#video = TinyTag.get(fileL)
# print(video)
"""
def get_media_properties(filename):

    result = subprocess.Popen(['hachoir-metadata', filename, '--raw', '--level=3'],
        stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

    results = result.stdout.read().decode('utf-8').split('\r\n')

    properties = {}

    for item in results:

        if item.startswith('- duration: '):
            duration = item.lstrip('- duration: ')
            if '.' in duration:
                t = datetime.datetime.strptime(item.lstrip('- duration: '), '%H:%M:%S.%f')
            else:
                t = datetime.datetime.strptime(item.lstrip('- duration: '), '%H:%M:%S')
            seconds = (t.microsecond / 1e6) + t.second + (t.minute * 60) + (t.hour * 3600)
            properties['duration'] = round(seconds)

        if item.startswith('- width: '):
            properties['width'] = int(item.lstrip('- width: '))

        if item.startswith('- height: '):
            properties['height'] = int(item.lstrip('- height: '))

    return properties

print(get_media_properties(fileL))
"""


"""
from pymdeco import services
srv = services.FileMetadataService()
meta = srv.get_metadata(fileL)
print(meta.to_json(indent=2))
"""
