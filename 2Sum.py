def twoSum(nums, target):
    nums.sort()
    hi = len(nums) - 1
    lo = 0
    while lo < hi:
        if (nums[lo] + nums[hi]) < target:
            lo += 1
        elif (nums[lo] + nums[hi]) > target:
            hi -= 1
        else:
            return [lo, hi]

