## Only verifies if a sudoku question is valid or not

def isValidSudoku(board):
	colHashes = []
	sudokuSize = 9
	gridSize = 3
	for col in range(sudokuSize):
		colHash = {}
		colHashes.append(colHash)
	for row in range(sudokuSize):
		rowHash = {}
		for col in range(sudokuSize):
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

	for gridRow in range(gridSize):
		for gridCol in range(gridSize):
			gridHash = {}
			for row in range(gridRow*gridSize,gridRow*gridSize+gridSize):
				for col in range(gridCol*gridSize,gridCol*gridSize+gridSize):
					if (board[row][col] != '.'):
						num = int(board[row][col])
						if num not in gridHash:
							gridHash[num] = 1
						else:
							return False


	return True

