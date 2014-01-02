#Matrix Library
#writen by Ryan Huard

#TODO: make this program able to take doubles instead of ints

import os

class Matrix:

	_matrix = []
	_rows = 0
	_cols = 0
	_pivots = []
	_operations = []

	def __init__(self):
		'''init method for class Matrix
		Initilize the matrix, receive the size and values of the matrix from the  user
		input: self
		output: 
		preconditions: an object of Matrix is created
		postconditions: the Matrix object will be initalized
		created: 25 Sep 2013
		last updated: 30 dec 2013

		update record:
			30 dec 2013: set to clear the consol window'''
		
		os.system("cls" if os.name == "nt" else "clear")
		con = True
		while(con == True):
			print("please enter the matrix you would like to use\n")
			self._rows = int(input("Please enter the number of rows: "))
			self._cols = int(input("Please enter the number of columns: "))
		
			for i in range(self._rows):
			
				#fill in each row of the matrix
				matrix_row = []
				for j in range(self._cols):
					matrix_row.append(float(input("please enter the number for location [" + str(i + 1) + "][" + str(j + 1) + "]")))
			
				self._matrix.append(matrix_row)

			#make sure the user put in the right matrix
			good = False
			print("\n***is this the right matrix?")
			
			answer = False
			while(answer == False):
				good = int(input("1-yes\n2-No\n"))
		
				if(good != 1 and good != 2):
					print("that was unrecognized please try again")
				else:
					answer = True
				
					if(good == 1):
						con = False
					else:
						con = True

		os.system("cls" if os.name == "nt" else "clear")

	
	def printMatrix(self):
		'''print Matrix
		prints out the matrix to the console window
		input: self
		output: void
		preconditions: the Matrix object will be made concrete
		postconditions: the Matrix object will be printed to the screen
		created: 25 sep 2013
		last updated: 30 Dec 2013

		update record:
			30 Dec 2013 - added the clear to the beginning of the function'''
		
		os.system("cls" if os.name == "nt" else "clear")
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
		self._operations.append("swap: row: " + str(row1 + 1) + " with row: " + str(row2 + 1))

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
		self._operations.append("scaled row: " + str(row + 1) + " by: " + str(scaler))

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
		self._operations.append("replaced row: " + str(row1 + 1) + " with row: " + str(row2 + 1) + " multiplyed by: " + str(scaler))
		
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

#end row operations, start program features

	def menu(self):
		'''Menu
		displays a menue for the start of the prgram
		input: void
		output: void
		preconditions: program will be started
		postconditions: the menu option will be executed
		created: 28 Dec 2013
		last update: 28 Dec 2013'''
	
		con = True
		while(con == True):	
			print("***WELCOME***\n***Matrix Reducton Program***")
			print("please enter a choice:")
			print("1-Manually Reduce Matrix")
			print("2-Automatically Reduce Matrix")
			print("0-Exit")

			choice = int(input("please enter your choice: "))
			
			if(choice != 1 and choice != 2 and choice != 0):
				print("I am sorry that was an unknown option, please try again")
				con = True
			else:
				con = False

		if(choice == 1):
			self.manualReduction()
			self.printMatrix()
			print("ths is your final matrix")
			self.printOperations()
		elif(choice == 2):
			self.automaticReduction()
			self.printMatrix()
			print("ths is your final matrix")
			self.printOperations()
		elif(choice == 0):
			quit()
		else:
			print("there was an error [0]")

	def manualReduction(self):
		'''Manual Reduction
		starts reducing the matrix by user input
		input: void
		output: void
		preconditions: the manual is chosen
		postconditions: the matrix can be manually reduced
		created: 28 Dec 2013
		last update: 30 Dec 2013

		update record:
			30 Dec 2013 - finished method'''
		
		finished = False
		while(finished == False):
			self.printMatrix()
			row_op = -1
			row_op =self.getRowOperation()
			if(row_op == 1): #TODO: get error checking into this function
				#scale
				row = int(input("please input the row you want to scale: ")) - 1
				scaler = float(input("please input the scaler you would want to scale by: "))
				self.scaleRow(row, scaler)
			elif(row_op == 2):
				#swap
				row1 = int(input("please enter the first row you would like to swap: ")) - 1
				row2 = int(input("please enter the second row you would like to swap: ")) - 1
				self.swapRow(row1, row2)
			elif(row_op == 3):
				#replace
				row1 = int(input("please enter the row you would like to replace: ")) - 1
				row2 = int(input("please enter the row you would like to replace the previous row with: ")) - 1
				scaler = float(input("please enter the scaler you would like to use for the replacement: "))
				self.replaceRow(row1, row2, scaler)
			elif(row_op == 0):
				#do nothing
				print("nothing will be changed in the matrix")
			else:
				print("There was an error [2] getting the wanted row operation. stopping execution")
				quit()
			self.printMatrix()
			#Check to see if done
			con = True
			while(con == True):
				choice = int(input("would you like to continue:\n1-Yes\n2-No\n:"))
				if(choice != 1 and choice != 2)
					print("I am sorry that is an invalid option, please try again")
				else:
					con = False
			if(choice == 1):
				finished = False #keep going
			else:
				finished = True #end

	def getRowOperation(self):
		'''Get Row Operation
		   gets the user input for the wanted row operation
		   input: void
		   output: an integer representing the wanted row operation
		   preconditions: manual reduction is running
		   postconditios: an operation will take place
		   created: 30 Dec 2013
		   last updated: 30 Dec 2013'''
		
		valid_choice = False
		while(valid_choice == False):
			print("what row operation would you like?")
			row_op = int(input("1-Scale\n2-Swap\n3-Replace\n0-Get Me Outta Here!!\n:"))

			if(row_op != 0 and row_op != 1 and row_op != 2 and row_op != 3):
				print("that was an invalid option please try again")
			else:
				valid_choice = True
		return row_op

	def automaticReduction(self):
		'''Automatic Reduction
		starts reducing the matrix automatically
		input: void
		output: void
		preconditions: the automatic option has been chosen
		postconditions: the matrix will be automatically reduced by the program
		created: 28 Dec 2013
		last updated: 28 Dec 2013'''
		print("this feature has not been implemented yet")
		input("please press any key to contine:")
		#TODO: Finish automatic Reduction

	def printOperations(self):
		'''Print Operations
		   prints out the list of what operations were used
		   input: void
		   output: void
		   preconditions: the operations that will take place have taken place
		   postconditions: a list will be printed with all of the operations
		   created: 1 Jan 2014
		   last updated: 1 jan 2014'''


		print("the operations that were used are:\n")
		for i in range(len(self._operations)):
			print(str(i) + " " + self._operations[i] + "\n")
