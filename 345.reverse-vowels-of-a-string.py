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
        vowels = []
        for c in s:
            if c in "aeiouAEIOU":
                vowels.append(c)
        for i in xrange(len(s)):
            if s[i] in "aeiouAEIOU":
                s[i] = vowels[-1]
                vowels.pop()
        return "".join(s)
