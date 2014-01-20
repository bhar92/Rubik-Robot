# This program snaps an image when you left click on the window
# In order to obtain the image, we are using an Android phone running the IP Webcam app
# You can download the app from https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en
# WARNING: The webcam MUST be used in 640x480 resolution or the program WILL NOT WORK

from SimpleCV import JpegStreamCamera, Display

def DrawSquare(pic, centerPoint, sideLength):
	# This function draws a square in the display
	boxWidth = sideLength
	boxHeight = boxWidth
	centerPointX = centerPoint[0]
	centerPointY = centerPoint[1]
	squareConrnerX = centerPointX - boxWidth / 2
	squareConrnerY = centerPointY - boxHeight / 2
	pic.drawRectangle(squareConrnerX, squareConrnerY, boxWidth, boxHeight)
	return

windowSize = (640,480)
# Initialize the webcam by providing URL to the camera
cam = JpegStreamCamera("http://192.168.2.100:8080/video?submenu=mjpg") 
i = 1
display = Display(windowSize)
img = cam.getImage()
img.save(display)
while not display.isDone():
	img = cam.getImage()
	DrawSquare(img, (320,240), 300)
	img.save(display)
	if display.mouseLeft:
		img.save("SquareCube" + str(i) +".jpg")
		img.drawText("Photo saved.")
		img.save(display)
		i = i + 1
	


