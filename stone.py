# Three stones are on a number line at positions a, b, and c.

# Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints.  Formally, let's say the stones are currently at positions x, y, z with x < y < z.  You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

# The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

# When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

 

# Example 1:

# Input: a = 1, b = 2, c = 5
# Output: [1,2]
# Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

# Example 2:

# Input: a = 4, b = 3, c = 2
# Output: [0,0]
# Explanation: We cannot make any moves.

# Example 3:

# Input: a = 3, b = 5, c = 1
# Output: [1,2]
# Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.

 

# Note:

#     1 <= a <= 100
#     1 <= b <= 100
#     1 <= c <= 100
#     a != b, b != c, c != a

 
def sum(a, b, c):
    count = (b-a - 1) + (c-b - 1)
    return count

def numMove(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """
    list = [a,b,c]
    list.sort()
    max_num = sum(list[0],list[1],list[2])
    min_num = 0
    print(list)
    if (max_num != 0):
        if (list[2] - list[1] == 2) or (list[2] - list[1] == 1) or (list[1] - list[0] == 1) or (list[1] - list[0] == 2):
            min_num = 1
        else:
            min_num = 2

    return [min_num,max_num]

print(numMoves(1,2,5))

class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        return numMove(a,b,c)


