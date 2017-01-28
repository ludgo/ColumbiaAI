import sys, string



def toArray(str):
	arr = []
	for i in xrange(3):
		arr.append([])
		for j in xrange(3):
			arr[i].append(str[3*i+j])
	return arr

class Board(object):

	def __init__(self, board):
		nocommas = string.replace(board, ",", "")
		self.blank = string.index(nocommas, "0")
		print self.blank
		self.array = toArray(nocommas)
		print self.array


method = sys.argv[1]
board = sys.argv[2]

b = Board(board)






