def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retList = []
        myDict = {}
        nums.sort()
        if nums[0] > 0 or nums[len(nums) - 1] < 0:
            break
        for lo in range(len(nums)-2):
        	hi = len(nums)-1
        	iter8 = lo + 1
        	while iter8 < hi:
        		arr = [nums[lo],nums[iter8],nums[hi]]
        		if sum(arr) == 0:
        			if str(arr) in myDict:
        				myDict[str(arr)] += 1
        				iter8 += 1
        				hi -= 1
        			else: 
        				retList.append(arr)
        				myDict[str(arr)] = 1
        				iter8 += 1
        				hi -= 1
        		if sum(arr) > 0:
        			hi -= 1
        		if sum(arr) < 0:
        			iter8 += 1
        return retList
