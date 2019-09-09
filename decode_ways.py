class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        num_ways = [0]*(len(s) + 1)
        num_ways[0] = 1
        if s[0] != '0':
            num_ways[1] = 1
        for i in range(2,len(s)+1):
            digit = int(s[i-1])
            digits = int(s[i-2]+s[i-1])
            if digit >= 1:
                num_ways[i] += num_ways[i-1]
            if digits >= 10 and digits <= 26:
                num_ways[i] += num_ways[i-2]
        return num_ways[len(s)]
