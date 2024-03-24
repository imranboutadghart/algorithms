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

def alpha_beta(board, isMax: bool, depth = 0):
	indepth = 9 - board.count(' ')
	if indepth == 9:
		return 0
	board_values = [0 for i in range(9)]
	fun = max if isMax else min
	for i in range(9):
		if board[i] != ' ':
			board_values[i]= '-'
			continue
		coe = 1 if isMax else -1
		player = 'x' if isMax else 'o'
		if won(board, 'x'):
			if (isMax): return 1
			board_values[i] = 1
		elif won(board, 'o'):
			if (not isMax): return -1
			board_values[i] = -1
		else:
			tmp = board.copy()
			tmp[i] = player
			board_values[i] = alpha_beta(tmp, not isMax, depth + 1)
			if fun(board_values[i], 0) != 0: return board_values[i]
	if depth == 0:
		nboard_values = [i if i != '-' else 10 * - fun(1, -1) for i in board_values]
		return nboard_values.index(fun(nboard_values))
	board_values = [i for i in board_values if i != '-']
	return fun(board_values)

for i in range(0, 9):
	if i % 2 == 0:
		board[alpha_beta(board, True)] = 'x'
	else:
		board[alpha_beta(board, False)] = 'o'
	if won(board, 'x') or won(board, 'o'):
		break
printboard(board)