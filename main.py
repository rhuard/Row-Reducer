#created by Ryan Huard
#this program row reduces a matrix
#	it cannot reduce matricies with complex numbers

#created:25 sep 2013
#last updated: 30 sep 2013
#	update notes:
#	-made Matrix.py the library and seperated main from that file

import Matrix as M

def main():

	##create matrix object and runs the program	
	matrix = M.Matrix()
	matrix.menu()#menu starts running the program


main()
