# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must
#  be a substring, "pwke" is a subsequence and not a substring.
# return type must be an int signifying the length of the unique substring


def isUnique(s):
    return (len(s) == len(set(s)))

def firstRepChar(s):
    dic = {}
    for c in s:
        if c not in dic:
            dic[c] = 1
        else:
            return c
    return '\n'

def longestUniqueSub(s):
    if len(s) <= 1:
        return len(s)
    if isUnique(s):
        return len(s)
    else:
        repChar = firstRepChar(s)
        repIndex1 = s.index(repChar)
        repIndex2 = repIndex1 + s[repIndex1+1:].index(repChar) + 1
        substring1 = s[:repIndex2]
        substring2 = s[repIndex1+1:]
        len1 = len(substring1)
        len2 = longestUniqueSub(substring2)
        return max(len1, len2)

