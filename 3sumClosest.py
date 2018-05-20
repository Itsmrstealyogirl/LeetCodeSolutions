## Parameters are list of numbers and the target sum
## Return the 3sum that is closest to the target

def 3sumClosest(nums, target):
	nums.sort()
	for head in range(len(nums) - 2):
		tail = len(nums) - 1
		iter8 = head + 1
		sum1 = nums[tail] + nums[head] + nums[iter8]
		while iter8 < tail:
			