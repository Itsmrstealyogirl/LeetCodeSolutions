def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retList = []
        hi = len(nums)-1
        iter8 = 1
        nums.sort()
        for lo in range(len(nums)) and hi in range(len(nums) - 1, lo, -1):