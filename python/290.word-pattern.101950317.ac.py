#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern
#
# Easy (32.62%)
# Total Accepted:    75888
# Total Submissions: 231734
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# ⁠Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Examples:
# 
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# 
# 
# 
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
# 
# 
# Credits:Special thanks to @minglotus6 for adding this problem and creating
# all test cases.
#
class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(str) == 0:
            return True
        strs = str.split()
        if len(strs) != len(pattern):
            return False
        table = dict()
        for i in xrange(len(strs)):
            if pattern[i] in table:
                if table[pattern[i]] != strs[i]:
                    return False
            elif strs[i] in table.values():
                return False
            else:
                table[pattern[i]] = strs[i]
        return True

