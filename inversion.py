# A subsequence is created by deleting zero or more elements from a list while maintaining the order. For example, the subsequences of [1,2,3] are [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]. AJ has a list of prices in an array. He considers an inversion to be any time there is a strictly decreasing subsequence of length 3.

 

# More formally, given an array, p = [p[0], p[1], …, p[n-1]], he considers an inversion in the array to be any time some p[i] > p[j] > p[k] and  i < j < k.

 

# Determine the number of inversions within a given array. For example, the array prices = [5,3,4,2,1]. Its inversions are:

# 	[5,3,2]
# 	[5,3,1]
# 	[5,4,2]
# 	[5,4,1]
# 	[5,2,1]
# 	[3,2,1]
# 	[4,2,1]

 

# Function Description 

# Complete the function maxInversions in the editor below. The function must return a long integer denoting the number of inversions in the array.

 

# maxInversions has the following parameter(s):

#     prices[prices[0],...prices[n-1]]:  an array of integers

 

# Constraints

#     1 ≤ n ≤ 5000
#     1 ≤ prices[i] ≤ 106, where 0 ≤ i < n

 
# Input Format for Custom Testing

# Input from stdin will be processed as follows and passed to the function.

 

# The first line contains an integer n, the size of the array prices.

# Each of the next n lines contains an integer prices[i].

 
# Sample Case 0

# Sample Input 0

# 5
# 4
# 1
# 3
# 2
# 5

 

# Sample Output 0

# 1

 

# Explanation 0

# prices = [4,1,3,2,5]

# There is only one inversion in the array: (4, 3, 2).

 
# Sample Case 1

# Sample Input 1

# 5
# 15
# 10
# 1
# 7
# 8

 

# Sample Output 1

# 3

 

# Explanation 1

# prices = [15,10,1,7,8]

# There are three inversions in the array: (15, 10, 1), (15, 10, 7), and (15, 10, 8).

 


def maxInversions(prices):
	
