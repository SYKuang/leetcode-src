#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (39.48%)
# Total Accepted:    113.2K
# Total Submissions: 286.8K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
#
#
# Example 1:
# Given s = "hello", return "holle".
#
#
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
#
#
# Note:
# The vowels does not include the letter "y".
#
#


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s)-1
        while start < end:
            while start < end and s[start] not in "aeiouAEIOU":
                start += 1
            while start < end and s[end] not in "aeiouAEIOU":
                end -= 1
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)
