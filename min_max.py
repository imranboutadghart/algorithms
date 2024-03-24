board=[	' ', ' ', ' ',
		' ', ' ', ' ',
		' ', ' ', ' ']

def won(board, n):
	if board[0] == n and board[1] == n and board[2] == n: return True
	if board[3] == n and board[4] == n and board[5] == n: return True
	if board[6] == n and board[7] == n and board[8] == n: return True

	if board[0] == n and board[3] == n and board[6] == n: return True
	if board[1] == n and board[4] == n and board[7] == n: return True
	if board[2] == n and board[5] == n and board[8] == n: return True

	if board[0] == n and board[4] == n and board[8] == n: return True
	if board[2] == n and board[4] == n and board[6] == n: return True

	return False

def printboard(board):
	for i in range(3):
		print(" ", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2])
		print(" - - - - - -")
	print("\n", end="")

def min_max(board, isMax: bool, depth = 0):
	if board.count(' ') == 0:
		return 0
	if won(board, 'x'): return 1
	if won(board, 'o'): return -1

	board_values = []
	for i in range(9):
		if board[i] != ' ':
			board_values.append(-2 if isMax else 2)
			continue
		player = 'x' if isMax else 'o'
		tmp = board.copy()
		tmp[i] = player
		board_values.append(min_max(tmp, not isMax, depth + 1))
	fun = max if isMax else min
	best = fun(board_values)
	index = board_values.index(best)
	return index if depth == 0 else best


for i in range(9):
	if i % 2 == 0:
		board[min_max(board, True)] = 'x'
	else:
		board[min_max(board, False)] = 'o'
	printboard(board)
	if won(board, 'x') or won(board, 'o'):
		break