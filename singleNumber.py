class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # approach: by drawing truth table for 00 -> 01 -> 10 -> 00
        #           l' = ~h & (l ^ i)
        #           h' = ~l' & (h ^ i)
        
        low_bits = high_bits = 0
        for num in nums:
            low_bits = ~high_bits & (low_bits ^ num)
            high_bits = ~low_bits & (high_bits ^ num)
        return low_bits
