# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


def spiral_walk(matrix):
    spiral_list = []
    if (len(matrix) == 0):
        return []
    if (len(matrix) == 1):
        return matrix[0]
    if (len(matrix[0]) == 1):
        for i in range(len(matrix)):
            spiral_list.append(matrix[i][0])
        return spiral_list
    
    num_spiral = int((len(matrix) + 1)/2)
    num_items = 0
    total = len(matrix[0]) * len(matrix)
    for i in range(num_spiral):
        if (num_items == total):
            break
        for col in range(i, len(matrix[0]) - i ):
            spiral_list.append(matrix[i][col])
            num_items += 1
        if (num_items == total):
            break
        for row in range(i+1, len(matrix) - i):
            spiral_list.append(matrix[row][len(matrix[0]) - 1 - i])
            num_items += 1
        if (num_items == total):
            break
        for col in range(len(matrix[0]) - 1 - i - 1, i, -1):
            spiral_list.append(matrix[len(matrix) - 1 - i][col])
            num_items += 1
        if (num_items == total):
            break
        for row in range(len(matrix) - 1 - i, i, -1):
            spiral_list.append(matrix[row][i])
            num_items += 1
    return spiral_list

#print(spiral_walk([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))
print(spiral_walk([[2,3,4],[5,6,7],[8,9,10],[11,12,13]]))

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return spiral_walk(matrix)

