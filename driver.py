import sys, resource, time, string
from model import Board, State
from util import writeFile


dic = {'path_to_goal': [], 'cost_of_path': 0, 'nodes_expanded': 0, 'fringe_size': 0, 'max_fringe_size': 0, 'search_depth': 0, 'max_search_depth': 0, 'running_time': '0.0', 'max_ram_usage': '0.0'}


def bfs(initState, goalSeq):
	queue = []
	inqueue = {}
	explored = {}
	queue.append(initState)
	inqueue[initState.board.seq] = 1

	while len(queue) > 0:
		dic['max_fringe_size'] = max(dic['max_fringe_size'], len(queue))

		st = queue.pop(0)
		inqueue[st.board.seq] = 0
		explored[st.board.seq] = 1
		st.findChildren()

		if st.board.seq == goalSeq:
			dic['search_depth'] = st.depth
			dic['fringe_size'] = len(queue)
			return st

		dic['nodes_expanded'] = dic['nodes_expanded'] + 1

		for child in st.udlr:
			if not child:
				continue
			try:
				if explored[child.board.seq] == 1:
					continue
			except KeyError:
				pass
			try:
				if inqueue[child.board.seq] == 1:
					continue
			except KeyError:
				pass

			queue.append(child)
			inqueue[child.board.seq] = 1
			dic['max_search_depth'] = max(dic['max_search_depth'], child.depth)

	return None

def dfs(initState, goalSeq):
	stack = []
	instack = {}
	explored = {}
	stack.append(initState)
	instack[initState.board.seq] = 1

	while len(stack) > 0:
		dic['max_fringe_size'] = max(dic['max_fringe_size'], len(stack))

		st = stack.pop()
		instack[st.board.seq] = 0
		explored[st.board.seq] = 1
		st.findChildren()

		if st.board.seq == goalSeq:
			dic['search_depth'] = st.depth
			dic['fringe_size'] = len(stack)
			return st

		dic['nodes_expanded'] = dic['nodes_expanded'] + 1

		for child in reversed(st.udlr):
			if not child:
				continue
			try:
				if explored[child.board.seq] == 1:
					continue
			except KeyError:
				pass
			try:
				if instack[child.board.seq] == 1:
					continue
			except KeyError:
				pass

			stack.append(child)
			instack[child.board.seq] = 1
			dic['max_search_depth'] = max(dic['max_search_depth'], child.depth)

	return None


method = sys.argv[1]
board = string.replace(sys.argv[2], ',', '')

root = State( Board(board), 0 )

bottom = None
if method == 'bfs':
	
	start_time = time.time()
	bottom = bfs(root, '012345678')
	dic['running_time'] = '%s' % round(time.time() - start_time, 8)

elif method == 'dfs':
	
	start_time = time.time()
	bottom = dfs(root, '012345678')
	dic['running_time'] = '%s' % round(time.time() - start_time, 8)

elif method == 'last':
	pass

elif method == 'ada':
	pass

dic['max_ram_usage'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

while bottom:
	if bottom.move:
		dic['path_to_goal'].insert(0, bottom.move)
		dic['cost_of_path'] = dic['cost_of_path'] + 1
	bottom = bottom.parent

writeFile(dic)


