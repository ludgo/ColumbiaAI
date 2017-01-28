import sys, string, copy


def toArray(str):
	arr = []
	for i in xrange(9):
		arr.append(str[i])
	return arr

def swap(array, indexA, indexB):
	c = []
	c = copy.copy(array)
	c[indexA] = array[indexB]
	c[indexB] = array[indexA]
	print array
	print c
	return c

class Board(object):

	def __init__(self, board):
		nocommas = string.replace(board, ",", "")
		self.blank = string.index(nocommas, "0")
		self.array = toArray(nocommas)

	def up(self):
		pos = self.blank - 3
		if pos in range(9):
			return swap(self.array, pos, self.blank)
		return None

method = sys.argv[1]
board = sys.argv[2]

b = Board(board)
b.up()





