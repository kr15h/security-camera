import time
import picamera

delay = 0.5

camera = picamera.PiCamera()
camera.resolution = (800, 600)

while True:
	ts = time.time()
	filename = 'images/image-' + str(ts) + '.jpg'
	camera.capture(filename)
	time.sleep(delay)
