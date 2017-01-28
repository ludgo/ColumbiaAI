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

	def __init__(self, board, depth, parent=None, move=None):
		self.board = board
		self.depth = depth
		self.parent = parent
		self.move = move
		self.udlr = [None, None, None, None]

	def findChildren(self):
		if self.move != "Down":
			b = self.board.up()
			if b:
				self.udlr[0] = State(b, self.depth + 1, self, "Up")
		if self.move != "Up":
			b = self.board.down()
			if b:
				self.udlr[1] = State(b, self.depth + 1, self, "Down")
		if self.move != "Right":
			b = self.board.left()
			if b:
				self.udlr[2] = State(b, self.depth + 1, self, "Left")
		if self.move != "Left":
			b = self.board.right()
			if b:
				self.udlr[3] = State(b, self.depth + 1, self, "Right")


