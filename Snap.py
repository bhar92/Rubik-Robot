from SimpleCV import JpegStreamCamera, Display
# Initialize the webcam by providing URL to the camera

def DrawSquare(pic, centerPoint, sideLength):
	boxWidth = sideLength
	boxHeight = boxWidth
	centerPointX = centerPoint[0]
	centerPointY = centerPoint[1]
	squareConrnerX = centerPointX - boxWidth / 2
	squareConrnerY = centerPointY - boxHeight / 2
	pic.drawRectangle(squareConrnerX, squareConrnerY, boxWidth, boxHeight)
	return

windowSize = (640,480)
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
	


