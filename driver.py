import sys, string
from Queue import Queue
from model import Board, State



def bfs(initState, goalSeq):
	q = Queue(100000)
	q.put(initState)
	explored = []

	while not q.empty():
		st = q.get()
		st.findChildren()
		explored.append(st.board.seq)

		if st.board.seq == goalSeq:
			return st

		for child in st.udlr:
			if child and child.board.seq not in explored:
				q.put(child)

	return None

method = sys.argv[1]
board = string.replace(sys.argv[2], ",", "")

root = State( Board(board) )

if method == "bfs":
	last = bfs(root, "012345678")
	print last.board.seq



