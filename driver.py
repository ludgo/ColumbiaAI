import sys, string
from Queue import Queue
from model import Board, State

dic = {'path_to_goal': [], 'cost_of_path': 0, 'nodes_expanded': 0, 'fringe_size': 0, 'max_fringe_size': 0, 'search_depth': 0, 'max_search_depth': 0, 'running_time': 0.0, 'max_ram_usage': 0.0}

def bfs(initState, goalSeq):
	q = Queue(100000)
	q.put(initState)
	explored = []

	while not q.empty():
		st = q.get()
		st.findChildren()
		explored.append(st.board.seq)

		if st.board.seq == goalSeq:
			dic['search_depth'] = st.depth
			return st

		for child in st.udlr:
			if child and child.board.seq not in explored:
				q.put(child)
				dic['nodes_expanded'] = dic['nodes_expanded'] + 1
				dic['max_search_depth'] = max(dic['max_search_depth'], child.depth)

	return None

method = sys.argv[1]
board = string.replace(sys.argv[2], ",", "")

root = State( Board(board), 0 )

if method == "bfs":
	bottom = bfs(root, "012345678")

	while bottom:
		if bottom.move:
			dic['path_to_goal'].insert(0, bottom.move)
			dic['cost_of_path'] = dic['cost_of_path'] + 1
		bottom = bottom.parent

	print dic


