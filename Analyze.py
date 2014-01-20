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
	# This function prints the image with alphabets corresponding to the colors
	for i in range(0,3):
		for j in range(0,3):
			img.drawText(stickerColors[i][j], 210 + 100*j, 120 + 100*i, color = Color.WHITE, fontsize = 48)
			img.show()
	return


img = Image("SquareCube.jpg") # Obtain image with cube within the red square
test = {}			# Dictionary containing difference images of a particular sticker and standard colors 
pixValues = []		# List containing the pixel values from (20,50) to (20,80) of each image present in test
averagesDict = {}	# Dictionary containing the average of pixValues corresponding to each color
averagesList = []	# List containing all the average of pixValues corresponding to each color
stickerColors = [[],[],[]] # Contains first letter of color of all the stickers in a picture

# Coordinates corresponding to the 'origin' of the cube
squareCornerX = 170	
squareCornerY = 90

for i in range(0,3):
	for j in range(0,3):
		croppedImg = img.crop(squareCornerX + j*100, squareCornerY + i*100, 100, 100) # Obtain just the sticker
		
		# Find the difference image of the sticker and all the standard colors and store it in test 
		for color in rubikColor:
			test[color] = croppedImg.colorDistance(color = rubikColor[color])
		
			# Obtain values of a line in the middle of the difference image
			# From observation, we see best results with pixels from (20,50) to (80,50)
			for j1 in range(20,81):
				pixValues.append(test[color].getPixel(j1,50)[0])
		
			average = np.average(pixValues)	# Find average of pixel values
			averagesList.append(average)	# And add the value to averagesList
			averagesDict[color] = average   # And also add the value to averagesDict
			pixValues = []					# Clear pixValues
		
		minAvg = np.amin(averagesList)	# Find the least average
		inv_averagesDict = {v:k for k, v in averagesDict.items()}	# Invert the dictionary
		stickerColors[i].append(inv_averagesDict[minAvg][0].upper())# Find the color corresponding to minAvg
		averagesDict = {}
		averagesList = []

PrintStickerColorOnImg(stickerColors)