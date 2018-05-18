## Only verifies if a sudoku question is valid or not

def isValidSudoku(board):
	colHashes = []
	for col in range(len(board[0])):
		colHash = {}
		colHashes.append(colHash)
	for row in range(len(board)):
		rowHash = {}
		for col in range(len(board[0])):
			if (board[row][col] != '.'):
				num = int(board[row][col])
				if num not in rowHash:
					rowHash[num] = 1
				else:
					return False
				if num not in colHashes[col]:
					colHashes[col][num] = 1
				else:
					return False
	return True

