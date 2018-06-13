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
        index = {c: i for i, c in enumerate(s)}
        counter = collections.Counter(s)
        res = len(s)
        for k in counter:
            if counter[k] == 1 and index[k] < res:
                res = index[k]
        return -1 if res == len(s) else res
