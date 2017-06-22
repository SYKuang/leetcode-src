#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings
#
# Easy (33.24%)
# Total Accepted:    102847
# Total Submissions: 308043
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note:
# You may assume both s and t have the same length.
#
class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Record the last index of the character
        if len(s) != len(t):
            return False
        hash1 = [-1 for i in range(255)]
        hash2 = [-1 for i in range(255)]
        for i in range(len(s)):
            if hash1[ord(s[i])] != hash2[ord(t[i])]:
                return False
            hash1[ord(s[i])] = i
            hash2[ord(t[i])] = i
        return True

