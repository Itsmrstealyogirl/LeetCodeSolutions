
class Solution:
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while (start < end):
            mid = start + (end-start) // 2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid
        return start
        
