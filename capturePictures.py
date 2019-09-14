from picamera import PiCamera
from time import sleep

camera = PiCamera()

# display camera view
camera.start_preview()
sleep(5)
camera.stop_preview()

# capture one photo
camera.start_preview()
sleep(5)
camera.capture('/image.jpg')
camera.stop_preview()

# capture five photos
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('image%s.jpg' % i)
camera.stop_preview()