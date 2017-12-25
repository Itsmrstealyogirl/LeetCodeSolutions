#Given a string, find the length of the longest substring without repeating characters.
#
#Examples:
#
#Given "abcabcbb", the answer is "abc", which the length is 3.
#
#Given "bbbbb", the answer is "b", with the length of 1.
#
#Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# return type must be an int signifying the length of the unique substring 
def isUnique(s):
	myDict = {}
	for c in s:
		myDict[c] += 1
	for key in myDict:
		if myDict[key] > 1:
			return False
	return True


def longestUniqueSub(s):
	if len(s) <= 1:
		return s
	if isUnique(s):
		return s
	else:
		temp1 = longestUniqueSub(s[1:])
		temp2 = longestUniqueSub(s[:1])
		if len(temp1)>len(temp2):
			return temp1
		else:
			return temp2

	