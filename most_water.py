
# Given n non-negative integers a1, a2, ..., an , 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return better_solution(height)




def naive_solution(list_n):
    area_list = []
    for i in range(len(list_n)):
        for j in range(i+1, len(list_n)):
            area_list.append(min(list_n[i], list_n[j]) * (j - i))
    return max(area_list)

def naive_dp(height):
    area_dict = {}




def better_solution(height):
    start_index = 0
    end_index = len(height) - 1
    max_area = min(height[start_index], height[end_index]) * (end_index - start_index)

    while (start_index < end_index):
        if (height[start_index] > height[end_index]):
            end_index -= 1
        else:
            start_index += 1

        max_area = max(max_area, min(height[start_index], height[end_index]) * (end_index - start_index))
    return max_area

print(better_solution([1,8,6,2,5,4,8,3,7]))
print(better_solution([1,7,6,7,5,2,4]))