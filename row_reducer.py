#created by Ryan Huard
#this program row reduces a matrix
#	it cannot reduce matricies with complex numbers

class Matrix:

	_matrix = []
	_rows = 0
	_cols = 0

	def __init__(self):

		self._rows = int(input("Please enter the number of rows: "))
		self._cols = int(input("Please enter the number of columns: "))
		
		for i in range(self._rows):
			
			#fill in each row of the matrix
			matrix_row = []
			for j in range(self._cols):
				matrix_row.append(int(input("please enter the number for location [" + str(i) + "][" + str(j) + "]")))
			
			self._matrix.append(matrix_row)

	
	def printMatrix(self):
		
		for i in range(self._rows):
			print("[ ", end = "")
			for j in range(self._cols):
				print(" " + str(self._matrix[i][j]) + " ", end = "")
			print(" ]")
		





def main():
	
	matrix = Matrix()
	matrix.printMatrix()



main()
