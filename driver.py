import sys, string
from model import Board, State


method = sys.argv[1]
board = string.replace(sys.argv[2], ",", "")

root = State( Board(board), 0 )





