# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Given input matrix = 
# b = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

# Example 2:

# Given input matrix =
# a = [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]

# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]


def solution(list):
    num_moves = int((len(list) + 1)//2)
    list_len = len(list)
    for i in range(num_moves):
        for offset in range(list_len - 2*i - 1):
            temp = list[i][i+offset]
            list[i][i+offset] = list[list_len -i - offset - 1][i]
            list[list_len -i - offset - 1][i] = list[list_len - i - 1][list_len-i - offset - 1]
            list[list_len - i - 1][list_len-i - offset - 1] = list[i+offset][list_len-i - 1]
            list[i+offset][list_len-i - 1] = temp

    return list

print(solution([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        