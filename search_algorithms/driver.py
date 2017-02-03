import sys, time
import string, math
import heapq
from model import Board, State
from util import writeFile, commaHash


dic = {'path_to_goal': [], 'cost_of_path': 0, 'nodes_expanded': 0, 'fringe_size': 0, 'max_fringe_size': 0, 'search_depth': 0, 'max_search_depth': 0, 'running_time': '0.0', 'max_ram_usage': '0.0'}


# breadth first search queue implementation
def bfs(initState, goalSeq):
	queue = []
	inqueue = {}
	explored = {}
	queue.append(initState)
	inqueue[commaHash(initState.board.seq)] = 1

	while len(queue) > 0:
		dic['max_fringe_size'] = max(dic['max_fringe_size'], len(queue))

		state = queue.pop(0)
		inqueue[commaHash(state.board.seq)] = 0
		explored[commaHash(state.board.seq)] = 1
		state.findChildren()

		if state.board.seq == goalSeq:
			dic['search_depth'] = state.depth
			dic['fringe_size'] = len(queue)
			return state

		dic['nodes_expanded'] = dic['nodes_expanded'] + 1

		for child in state.udlr:
			if not child:
				continue
			try:
				if explored[commaHash(child.board.seq)] == 1:
					continue
			except KeyError:
				pass
			try:
				if inqueue[commaHash(child.board.seq)] == 1:
					continue
			except KeyError:
				pass

			queue.append(child)
			inqueue[commaHash(child.board.seq)] = 1
			dic['max_search_depth'] = max(dic['max_search_depth'], child.depth)

	return None

# depth first search stack implementation
def dfs(initState, goalSeq):
	stack = []
	instack = {}
	explored = {}
	stack.append(initState)
	instack[commaHash(initState.board.seq)] = 1

	while len(stack) > 0:
		dic['max_fringe_size'] = max(dic['max_fringe_size'], len(stack))

		state = stack.pop()
		instack[commaHash(state.board.seq)] = 0
		explored[commaHash(state.board.seq)] = 1
		state.findChildren()

		if state.board.seq == goalSeq:
			dic['search_depth'] = state.depth
			dic['fringe_size'] = len(stack)
			return state

		dic['nodes_expanded'] = dic['nodes_expanded'] + 1

		for child in reversed(state.udlr):
			if not child:
				continue
			try:
				if explored[commaHash(child.board.seq)] == 1:
					continue
			except KeyError:
				pass
			try:
				if instack[commaHash(child.board.seq)] == 1:
					continue
			except KeyError:
				pass

			stack.append(child)
			instack[commaHash(child.board.seq)] = 1
			dic['max_search_depth'] = max(dic['max_search_depth'], child.depth)

	return None

# a-star first search heap implementation
def ast(initState, goalSeq):
	heap = []
	inheap = {}
	explored = {}
	heapq.heappush(heap, initState)
	inheap[commaHash(initState.board.seq)] = 1

	while len(heap) > 0:
		dic['max_fringe_size'] = max(dic['max_fringe_size'], len(heap))

		state = heapq.heappop(heap)
		inheap[commaHash(state.board.seq)] = 0
		explored[commaHash(state.board.seq)] = 1
		state.findChildren()

		if state.board.seq == goalSeq:
			dic['search_depth'] = state.depth
			dic['fringe_size'] = len(heap)
			return state

		dic['nodes_expanded'] = dic['nodes_expanded'] + 1

		for child in reversed(state.udlr):
			if not child:
				continue
			try:
				if explored[commaHash(child.board.seq)] == 1:
					continue
			except KeyError:
				pass
			try:
				if inheap[commaHash(child.board.seq)] == 1:
					continue
			except KeyError:
				pass

			heapq.heappush(heap, child)
			inheap[commaHash(child.board.seq)] = 1
			dic['max_search_depth'] = max(dic['max_search_depth'], child.depth)

	return None


method = sys.argv[1]
board = sys.argv[2].split(',')

N = int(math.sqrt(len(board)))
root = State( Board(board, N), 0 )

bottom = None
goal = []
for ch in range(N**2):
	goal.append(str(ch))

if method == 'bfs':
	
	start_time = time.time()
	bottom = bfs(root, goal)
	dic['running_time'] = '%s' % round(time.time() - start_time, 8)

elif method == 'dfs':
	
	start_time = time.time()
	bottom = dfs(root, goal)
	dic['running_time'] = '%s' % round(time.time() - start_time, 8)

elif method == 'ast':
	pass

	start_time = time.time()
	bottom = ast(root, goal)
	dic['running_time'] = '%s' % round(time.time() - start_time, 8)

elif method == 'ada':
	pass

try:
	import resource
	dic['max_ram_usage'] = '%s' % round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000, 8)
except:
	pass

while bottom:
	if bottom.move:
		dic['path_to_goal'].insert(0, bottom.move)
		dic['cost_of_path'] = dic['cost_of_path'] + 1
	bottom = bottom.parent

writeFile(dic)


