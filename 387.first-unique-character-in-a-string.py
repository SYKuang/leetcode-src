#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (47.29%)
# Total Accepted:    128.1K
# Total Submissions: 270.9K
# Testcase Example:  '"leetcode"'
#
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#
#


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s)
        for i in xrange(26):
            c = chr(ord('a')+i)
            cIndex = s.find(c)
            if cIndex != -1 and cIndex == s.rfind(c):
                res = min(res, cIndex)
        return -1 if res == len(s) else res
