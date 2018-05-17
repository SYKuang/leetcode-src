#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (60.47%)
# Total Accepted:    248.5K
# Total Submissions: 410.8K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and returns the string
# reversed.
#
#
# Example:
# Given s = "hello", return "olleh".
#
#


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
