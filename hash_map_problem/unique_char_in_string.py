# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.
class Solution(object):
    def firstUniqChar(self, s):
        seen ={}
  
        if len(s) == 0:
            return -1
        for i in range(0,len(s)):
            elem = s[i]
            if elem not in seen.keys():
                seen[elem] = 1
            else:
                seen[elem] += 1
            
        for i in range(0,len(s)):
            item = s[i]
            if seen[item] == 1:
                return i
        return -1
        """
        :type s: str
        :rtype: int
        """
        