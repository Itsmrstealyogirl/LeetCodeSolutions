## Only verifies if a sudoku question is valid or not

def isValidSudoku(board):
	colHashes = []
	for row in range(len(board)):
		rowHash = {}
		for col in range(len(board[0])):
			if (row == 0):
				colHashes[col] = {}
			if (board[row][col] != '.'):
				num = board[row][col]
				if num not in rowHash:
					rowHash[num] = 1
				else:
					return False
				if num not in colHashes[col]:
					colHashes[col][num] = 1
				else:
					return False
	return True

