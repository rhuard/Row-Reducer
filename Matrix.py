#Matrix Library
#writen by Ryan Huard

class Matrix:

	_matrix = []
	_rows = 0
	_cols = 0
	_pivots = []

	def __init__(self):
		'''init method for class Matrix
		Initilize the matrix, receive the size and values of the matrix from the  user
		input: self
		output: 
		preconditions: an object of Matrix is created
		postconditions: the Matrix object will be initalized
		created: 25 Sep 2013
		last updated: 25 sep 2013'''

		self._rows = int(input("Please enter the number of rows: "))
		self._cols = int(input("Please enter the number of columns: "))
		
		for i in range(self._rows):
			
			#fill in each row of the matrix
			matrix_row = []
			for j in range(self._cols):
				matrix_row.append(int(input("please enter the number for location [" + str(i) + "][" + str(j) + "]")))
			
			self._matrix.append(matrix_row)

	
	def printMatrix(self):
		'''print Matrix
		prints out the matrix to the console window
		input: self
		output: void
		preconditions: the Matrix object will be made concrete
		postconditions: the Matrix object will be printed to the screen
		created: 25 sep 2013
		last updated: 25 sep 2013'''
		
		for i in range(self._rows):
			print("[ ", end = "")
			for j in range(self._cols):
				print(" " + str(self._matrix[i][j]) + " ", end = "")
			print(" ]")
		
#row reduction operations
	def swapRow(self, row1, row2):
		'''Swap Row
		swaps two rows of a matrix
		input: self, row1 index and row2 index as integers
		output: void
		preconditions: a matrix object has been made concrete
		postconditions: the matrix object will have two rows swaped
		created: 30 sep 2013
		last updated: 30 sep 2013'''

		self._matrix[row1], self._matrix[row2] = self._matrix[row2], self._matrix[row1]

	def scaleRow(self, row, scaler):
		'''Scale Row
		scales a row by a scaler - this is acomplished by multiplecation, so if division is needed, pass in a fraction
		input: self, the row index as an integer and the scaler
		output: void
		preconditions: a matrix object has been made concrete
		postcondtions: the row of the matrix will be scaled
		created: 30 sep 2013
		last updated: 30 sep 2013'''

		for i in range(self._cols):
			self._matrix[row][i] *= scaler

	def replaceRow(self, row1, row2, scaler):
		'''Replace Row
		replaces a row with the sum of itself and a multiple of another row
		input: self, row1 index (the row being replaced) as an int, row2 index as an int, scaler
		output: void
		preconditions: a matrix object has been made concrete
		postconditions: the row of the matrix will be replaced
		created: 30 sep 2013
		last updated: 30 sep 2013'''

		for i in range(self._cols):
			self._matrix[row1][i] = self._matrix[row1][i] + (self._matrix[row2][i] * scaler)
		
	def findPivots(self):
		'''fine Pivots
		finds the pivots in the matrix
		input: void
		output: list of tuples of the indicies of a matrix
		preconditions: there is a concrete matrix
		postconditions: a list containg the the indecies as tuples will be returned
		created: 06 Nov 2013
		last updated: 06 Nov 2013'''

		has_pivot = False #the row already has a pivot
		pivots = []		

		for i in range(self._rows):
			for j in range(self._cols):
				if(self._matrix[i][j] != 0 and has_pivot == False):
					pivots.append((i,j))
					has_pivot = True

			has_pivot = False
		return pivots

	def isInEchelonForm(self):
		'''is in Echelon Form
		checks to see if the matrix is in echelon form
		input: void
		output: boolean
		preconditions: the matrix has been made concrete
		postconditions: a true or false will be returned based on if the matrix is in echelon form or not
		created: 06 Nov 2013
		last updated: 06 Nov 2013'''
		
		self._pivots = self.findPivots()
		#todo: finish this method


		



