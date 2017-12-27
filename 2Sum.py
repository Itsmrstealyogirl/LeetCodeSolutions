def twoSum(nums, target):
    temp = nums[:]
    nums.sort()
    hi = len(nums) - 1
    lo = 0
    while lo < hi:
        if (nums[lo] + nums[hi]) < target:
            lo += 1
        elif (nums[lo] + nums[hi]) > target:
            hi -= 1
        else:
            if nums[lo] == nums[hi]:
                return [temp.index(nums[lo]), temp[temp.index(nums[lo])+1:].index(nums[hi])+temp.index(nums[lo])+1]
            else:
                return [temp.index(nums[lo]), temp.index(nums[hi])]

