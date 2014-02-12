import numpy as np

Uf = 'Up Face'
Ff = 'Front Face'
Lf = 'Left Face'
Rf = 'Right Face'
Bf = 'Back Face'
Df = 'Down Face'

facesActualDict = {
		Uf: [   ['W','W','W'],['W','W','W'],['W','W','W']   ],
		Ff: [   ['G','G','G'],['G','G','G'],['G','G','G']   ],
		Rf: [   ['R','R','R'],['R','R','R'],['R','R','R']   ],
		Lf: [	['O','O','O'],['O','O','O'],['O','O','O']	],
		Bf: [   ['B','B','B'],['B','B','B'],['B','B','B']   ],
		Df: [   ['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']   ]
		}


facesUpdatedDict = {
		Uf: [],
		Ff: [],
		Lf: [],
		Rf: [],
		Bf: [],
		Df: []
	}

someList = []

def clearFacesUpdatedDict():
	for key in facesUpdatedDict.keys():
		facesUpdatedDict[key] = []
	return

def reverseBackFace():
		facesActualDict[Bf] = facesActualDict[Bf][::-1] 
		for row in range(0,len(facesActualDict[Bf])):
			facesActualDict[Bf][row] = facesActualDict[Bf][row][::-1]
		return

def move(direction):
	
	if direction == "U":
		fromList =  [Ff, Lf, Bf, Rf]
		toList =    [Lf, Bf, Rf, Ff]
	
		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesUpdatedDict[t].append( facesActualDict[f][0][i] )
	
		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesActualDict[t][0][i] = facesUpdatedDict[t][i]
			
		facesActualDict[Uf] = np.transpose(facesActualDict[Uf])

		temp = np.copy(facesActualDict[Uf][:, 0])
		facesActualDict[Uf][:, 0] = facesActualDict[Uf][:, 2]
		facesActualDict[Uf][:, 2] = temp
		clearFacesUpdatedDict()
		return
# ---------------------------------------------------------------------
	elif direction == "U'":
		fromList =  [Ff, Rf, Bf, Lf]
		toList =    [Rf, Bf, Lf, Ff]

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesUpdatedDict[t].append( facesActualDict[f][0][i] )
	
		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesActualDict[t][0][i] = facesUpdatedDict[t][i]

		facesActualDict[Uf] = np.transpose(facesActualDict[Uf])
		
		temp = np.copy(facesActualDict[Uf][0, :])
		facesActualDict[Uf][0, :] = facesActualDict[Uf][2, :]
		facesActualDict[Uf][2, :] = temp
		clearFacesUpdatedDict()
		return
# ---------------------------------------------------------------------
	elif direction == "L":
		reverseBackFace()

		fromList =  [Ff, Df, Bf, Uf]
		toList =    [Df, Bf, Uf, Ff]

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesUpdatedDict[t].append( facesActualDict[f][i][0] )

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesActualDict[t][i][0] = facesUpdatedDict[t][i]

		facesActualDict[Lf] = np.transpose(facesActualDict[Lf])
		
		temp = np.copy(facesActualDict[Lf][:, 0])
		facesActualDict[Lf][:, 0] = facesActualDict[Lf][:, 2]
		facesActualDict[Lf][:, 2] = temp

		reverseBackFace()
		clearFacesUpdatedDict()
		return
# ---------------------------------------------------------------------
	elif direction == "L'":
		reverseBackFace()

		fromList =  [Ff, Uf, Bf, Df]
		toList =    [Uf, Bf, Df, Ff]

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesUpdatedDict[t].append( facesActualDict[f][i][0] )

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesActualDict[t][i][0] = facesUpdatedDict[t][i]

		facesActualDict[Lf] = np.transpose(facesActualDict[Lf])
		
		temp = np.copy(facesActualDict[Lf][0, :])
		facesActualDict[Lf][0, :] = facesActualDict[Lf][2, :]
		facesActualDict[Lf][2, :] = temp

		reverseBackFace()
		clearFacesUpdatedDict()
		return
# ---------------------------------------------------------------------
	elif direction == "R":
		reverseBackFace()

		fromList =  [Ff, Uf, Bf, Df]
		toList =    [Uf, Bf, Df, Ff]

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesUpdatedDict[t].append( facesActualDict[f][i][2] )

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesActualDict[t][i][2] = facesUpdatedDict[t][i]

		facesActualDict[Rf] = np.transpose(facesActualDict[Rf])
		
		temp = np.copy(facesActualDict[Rf][:, 0])
		facesActualDict[Rf][:, 0] = facesActualDict[Rf][:, 2]
		facesActualDict[Rf][:, 2] = temp

		reverseBackFace()
		clearFacesUpdatedDict()
		return
# ---------------------------------------------------------------------
	elif direction == "R'":
		reverseBackFace()

		fromList =  [Ff, Df, Bf, Uf]
		toList =    [Df, Bf, Uf, Ff]

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesUpdatedDict[t].append( facesActualDict[f][i][2] )

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesActualDict[t][i][2] = facesUpdatedDict[t][i]

		facesActualDict[Rf] = np.transpose(facesActualDict[Rf])
		
		temp = np.copy(facesActualDict[Rf][0, :])
		facesActualDict[Rf][0, :] = facesActualDict[Rf][2, :]
		facesActualDict[Rf][2, :] = temp

		reverseBackFace()
		clearFacesUpdatedDict()
		return
# ---------------------------------------------------------------------
	elif direction == "F":
		
		# Here be dragons. It works. Don't change it.

		FromList =  [Rf, Df, Lf, Uf]
		toList =    [Df, Lf, Uf, Rf] # Not really needed for this

		facesUpdatedDict[Df].append( facesActualDict[Rf][0][0] )
		facesUpdatedDict[Df].append( facesActualDict[Rf][1][0] )
		facesUpdatedDict[Df].append( facesActualDict[Rf][2][0] )

		facesUpdatedDict[Lf].append( facesActualDict[Df][0][0] )
		facesUpdatedDict[Lf].append( facesActualDict[Df][0][1] )
		facesUpdatedDict[Lf].append( facesActualDict[Df][0][2] )
		
		facesUpdatedDict[Uf].append( facesActualDict[Lf][0][2] )
		facesUpdatedDict[Uf].append( facesActualDict[Lf][1][2] )
		facesUpdatedDict[Uf].append( facesActualDict[Lf][2][2] )

		facesUpdatedDict[Rf].append( facesActualDict[Uf][2][0] )
		facesUpdatedDict[Rf].append( facesActualDict[Uf][2][1] )
		facesUpdatedDict[Rf].append( facesActualDict[Uf][2][2] )		

		facesActualDict[Rf][0][0] = facesUpdatedDict[Rf][0]
		facesActualDict[Rf][1][0] = facesUpdatedDict[Rf][1]
		facesActualDict[Rf][2][0] = facesUpdatedDict[Rf][2]

		facesActualDict[Uf][2][0] = facesUpdatedDict[Uf][2]
		facesActualDict[Uf][2][1] = facesUpdatedDict[Uf][1]
		facesActualDict[Uf][2][2] = facesUpdatedDict[Uf][0]
		
		facesActualDict[Df][0][0] = facesUpdatedDict[Df][2]
		facesActualDict[Df][0][1] = facesUpdatedDict[Df][1]
		facesActualDict[Df][0][2] = facesUpdatedDict[Df][0]
		
		facesActualDict[Lf][0][2] = facesUpdatedDict[Lf][0]
		facesActualDict[Lf][1][2] = facesUpdatedDict[Lf][1]
		facesActualDict[Lf][2][2] = facesUpdatedDict[Lf][2]

		facesActualDict[Ff] = np.transpose(facesActualDict[Ff])
		
		temp = np.copy(facesActualDict[Ff][:, 0])
		facesActualDict[Ff][:, 0] = facesActualDict[Ff][:, 2]
		facesActualDict[Ff][:, 2] = temp

		clearFacesUpdatedDict()
		return
# ---------------------------------------------------------------------
	elif direction == "F'":
		
		# Here be dragons. It works. Don't change it.

		FromList =  [Rf, Uf, Lf, Df]
		toList =    [Uf, Lf, Df, Rf] # Not really needed for this

		facesUpdatedDict[Uf].append( facesActualDict[Rf][0][0] )
		facesUpdatedDict[Uf].append( facesActualDict[Rf][1][0] )
		facesUpdatedDict[Uf].append( facesActualDict[Rf][2][0] )

		facesUpdatedDict[Lf].append( facesActualDict[Uf][2][0] )
		facesUpdatedDict[Lf].append( facesActualDict[Uf][2][1] )
		facesUpdatedDict[Lf].append( facesActualDict[Uf][2][2] )
		
		facesUpdatedDict[Df].append( facesActualDict[Lf][0][2] )
		facesUpdatedDict[Df].append( facesActualDict[Lf][1][2] )
		facesUpdatedDict[Df].append( facesActualDict[Lf][2][2] )

		facesUpdatedDict[Rf].append( facesActualDict[Df][0][0] )
		facesUpdatedDict[Rf].append( facesActualDict[Df][0][1] )
		facesUpdatedDict[Rf].append( facesActualDict[Df][0][2] )		

		facesActualDict[Rf][0][0] = facesUpdatedDict[Rf][2]
		facesActualDict[Rf][1][0] = facesUpdatedDict[Rf][1]
		facesActualDict[Rf][2][0] = facesUpdatedDict[Rf][0]

		facesActualDict[Uf][2][0] = facesUpdatedDict[Uf][0]
		facesActualDict[Uf][2][1] = facesUpdatedDict[Uf][1]
		facesActualDict[Uf][2][2] = facesUpdatedDict[Uf][2]
		
		facesActualDict[Df][0][0] = facesUpdatedDict[Df][0]
		facesActualDict[Df][0][1] = facesUpdatedDict[Df][1]
		facesActualDict[Df][0][2] = facesUpdatedDict[Df][2]
		
		facesActualDict[Lf][0][2] = facesUpdatedDict[Lf][2]
		facesActualDict[Lf][1][2] = facesUpdatedDict[Lf][1]
		facesActualDict[Lf][2][2] = facesUpdatedDict[Lf][0]

		facesActualDict[Ff] = np.transpose(facesActualDict[Ff])
		
		temp = np.copy(facesActualDict[Ff][0, :])
		facesActualDict[Ff][0, :] = facesActualDict[Ff][2, :]
		facesActualDict[Ff][2, :] = temp

		clearFacesUpdatedDict()
		return
# ---------------------------------------------------------------------
	elif direction == "B":
		
		# Here be dragons. It works. Don't change it.				

		FromList =  [Rf, Uf, Lf, Df]
		toList =    [Uf, Lf, Df, Rf] # Not really needed for this

		facesUpdatedDict[Uf].append( facesActualDict[Rf][0][2] )
		facesUpdatedDict[Uf].append( facesActualDict[Rf][1][2] )
		facesUpdatedDict[Uf].append( facesActualDict[Rf][2][2] )

		facesUpdatedDict[Lf].append( facesActualDict[Uf][0][0] )
		facesUpdatedDict[Lf].append( facesActualDict[Uf][0][1] )
		facesUpdatedDict[Lf].append( facesActualDict[Uf][0][2] )
		
		facesUpdatedDict[Df].append( facesActualDict[Lf][0][0] )
		facesUpdatedDict[Df].append( facesActualDict[Lf][1][0] )
		facesUpdatedDict[Df].append( facesActualDict[Lf][2][0] )

		facesUpdatedDict[Rf].append( facesActualDict[Df][2][0] )
		facesUpdatedDict[Rf].append( facesActualDict[Df][2][1] )
		facesUpdatedDict[Rf].append( facesActualDict[Df][2][2] )		

		facesActualDict[Rf][0][2] = facesUpdatedDict[Rf][2]
		facesActualDict[Rf][1][2] = facesUpdatedDict[Rf][1]
		facesActualDict[Rf][2][2] = facesUpdatedDict[Rf][0]

		facesActualDict[Uf][0][0] = facesUpdatedDict[Uf][0]
		facesActualDict[Uf][0][1] = facesUpdatedDict[Uf][1]
		facesActualDict[Uf][0][2] = facesUpdatedDict[Uf][2]
		
		facesActualDict[Df][2][0] = facesUpdatedDict[Df][0]
		facesActualDict[Df][2][1] = facesUpdatedDict[Df][1]
		facesActualDict[Df][2][2] = facesUpdatedDict[Df][2]
		
		facesActualDict[Lf][0][0] = facesUpdatedDict[Lf][2]
		facesActualDict[Lf][1][0] = facesUpdatedDict[Lf][1]
		facesActualDict[Lf][2][0] = facesUpdatedDict[Lf][0]

		facesActualDict[Bf] = np.transpose(facesActualDict[Bf])
		
		temp = np.copy(facesActualDict[Bf][:, 0])
		facesActualDict[Bf][:, 0] = facesActualDict[Bf][:, 2]
		facesActualDict[Bf][:, 2] = temp

		clearFacesUpdatedDict()		
		return
# ---------------------------------------------------------------------
	elif direction == "B'":
		
		# ToDo

		FromList =  [Rf, Df, Lf, Uf]
		toList =    [Df, Lf, Uf, Rf] # Not really needed for this

		facesUpdatedDict[Df].append( facesActualDict[Rf][0][2] )
		facesUpdatedDict[Df].append( facesActualDict[Rf][1][2] )
		facesUpdatedDict[Df].append( facesActualDict[Rf][2][2] )

		facesUpdatedDict[Lf].append( facesActualDict[Df][2][0] )
		facesUpdatedDict[Lf].append( facesActualDict[Df][2][1] )
		facesUpdatedDict[Lf].append( facesActualDict[Df][2][2] )
		
		facesUpdatedDict[Uf].append( facesActualDict[Lf][0][0] )
		facesUpdatedDict[Uf].append( facesActualDict[Lf][1][0] )
		facesUpdatedDict[Uf].append( facesActualDict[Lf][2][0] )

		facesUpdatedDict[Rf].append( facesActualDict[Uf][0][0] )
		facesUpdatedDict[Rf].append( facesActualDict[Uf][0][1] )
		facesUpdatedDict[Rf].append( facesActualDict[Uf][0][2] )

		facesActualDict[Rf][0][2] = facesUpdatedDict[Rf][0]
		facesActualDict[Rf][1][2] = facesUpdatedDict[Rf][1]
		facesActualDict[Rf][2][2] = facesUpdatedDict[Rf][2]

		facesActualDict[Uf][0][0] = facesUpdatedDict[Uf][2]
		facesActualDict[Uf][0][1] = facesUpdatedDict[Uf][1]
		facesActualDict[Uf][0][2] = facesUpdatedDict[Uf][0]
		
		facesActualDict[Df][2][0] = facesUpdatedDict[Df][2]
		facesActualDict[Df][2][1] = facesUpdatedDict[Df][1]
		facesActualDict[Df][2][2] = facesUpdatedDict[Df][0]
		
		facesActualDict[Lf][0][0] = facesUpdatedDict[Lf][0]
		facesActualDict[Lf][1][0] = facesUpdatedDict[Lf][1]
		facesActualDict[Lf][2][0] = facesUpdatedDict[Lf][2]

		facesActualDict[Bf] = np.transpose(facesActualDict[Bf])
		
		temp = np.copy(facesActualDict[Bf][0, :])
		facesActualDict[Bf][0, :] = facesActualDict[Bf][2, :]
		facesActualDict[Bf][2, :] = temp

		clearFacesUpdatedDict()		
		return
# ---------------------------------------------------------------------
	elif direction == "D":
		
		fromList =  [Ff, Rf, Bf, Lf]
		toList =    [Rf, Bf, Lf, Ff] # Not really needed for this

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesUpdatedDict[t].append( facesActualDict[f][2][i] )

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesActualDict[t][2][i] = facesUpdatedDict[t][i]

		facesActualDict[Df] = np.transpose(facesActualDict[Df])
		
		temp = np.copy(facesActualDict[Df][:, 0])
		facesActualDict[Df][:, 0] = facesActualDict[Df][:, 2]
		facesActualDict[Df][:, 2] = temp

		clearFacesUpdatedDict()		
		return
# ---------------------------------------------------------------------
	elif direction == "D'":
		
		fromList =  [Ff, Lf, Bf, Rf]
		toList =    [Lf, Bf, Rf, Ff] # Not really needed for this

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesUpdatedDict[t].append( facesActualDict[f][2][i] )

		for f,t in zip(fromList, toList):
			for i in range(0,3):
				facesActualDict[t][2][i] = facesUpdatedDict[t][i]

		facesActualDict[Df] = np.transpose(facesActualDict[Df])
		
		temp = np.copy(facesActualDict[Df][0, :])
		facesActualDict[Df][0, :] = facesActualDict[Df][2, :]
		facesActualDict[Df][2, :] = temp

		clearFacesUpdatedDict()	
		return