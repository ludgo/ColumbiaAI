import string
from util import swap

class Board(object):

	def __init__(self, board):
		self.seq = board
		self.blank = string.index(board, "0")

	def up(self):
		pos = self.blank - 3
		if pos in range(9):
			return Board( swap(self.seq, pos, self.blank) )
		return None

	def down(self):
		pos = self.blank + 3
		if pos in range(9):
			return Board( swap(self.seq, pos, self.blank) )
		return None

	def left(self):
		pos = self.blank - 1
		if pos % 3 != 2:
			return Board( swap(self.seq, pos, self.blank) )
		return None

	def right(self):
		pos = self.blank + 1
		if pos % 3 != 0:
			return Board( swap(self.seq, pos, self.blank) )
		return None

class State(object):

	def __init__(self, Board, depth):
		self.board = Board
		self.upChild = self.board.up()
		self.downChild = self.board.down()
		self.leftChild = self.board.left()
		self.rightChild = self.board.right()
		self.depth = depth
		print "---"
		print self.board
		print self.upChild
		print self.downChild
		print self.leftChild
		print self.rightChild
		print self.depth
		print "-----"


