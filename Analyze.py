from SimpleCV import Image,Color
import numpy as np

# Dictionary of standard rubik's cube sticker colors
rubikColor = {'red':(204, 0, 34),
			'green':(0, 158, 96),
			'blue':(0, 81, 186),
			'orange':(255, 69, 0),
			'yellow':(255, 213, 0),
			'white':(255, 255, 255)}

def PrintStickerColorOnImg(stickerColors):
	for i in range(0,3):
		for j in range(0,3):
			img.drawText(stickerColors[i][j], 210 + 100*j, 120 + 100*i, color = Color.WHITE, fontsize = 48)
			img.show()
	return


img = Image("SquareCube1.jpg")
test = {}
averagesDict = {}
averagesList = []
pixValues = []
stickerColors = [[],[],[]]

squareCornerX = 170
squareCornerY = 90

for i in range(0,3):
	for j in range(0,3):

		croppedImg = img.crop(squareCornerX + j*100,squareCornerY + i*100,100,100)
		for color in rubikColor:
			test[color] = croppedImg.colorDistance(color = rubikColor[color])
			for j1 in range(20,81):
				pixValues.append(test[color].getPixel(j1,50)[0])
		
			average = np.average(pixValues)
			averagesList.append(average)
			averagesDict[color] = average
			pixValues = []
		
		minAvg = np.amin(averagesList)
		inv_averagesDict = {v:k for k, v in averagesDict.items()}
		stickerColors[i].append(inv_averagesDict[minAvg][0].upper())
		averagesDict = {}
		averagesList = []

PrintStickerColorOnImg(stickerColors)