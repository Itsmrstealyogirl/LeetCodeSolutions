# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true

# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        digits = []
        while(x != 0):
            digit = x%10
            x -= digit
            x /= 10
            digits.append(digit)
        l = 0
        r = len(digits)-1
        flag = 1
        while(l <= r):
            if digits[l] != digits[r]:
                flag = 0
                break
            l+=1
            r-=1
        if flag == 1:
            return True
        else:
            return False

