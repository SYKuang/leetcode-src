#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram
#
# Easy (45.74%)
# Total Accepted:    154753
# Total Submissions: 336828
# Testcase Example:  '""\n""'
#
# Given two strings s and t, write a function to determine if t is an anagram
# of s. 
# 
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        table1 = [0 for i in xrange(255)]
        table2 = [0 for i in xrange(255)]
        for i in xrange(len(s)):
            table1[ord(s[i])] = table1[ord(s[i])] + 1
            table2[ord(t[i])] = table2[ord(t[i])] + 1
        for i in xrange(255):
            if table1[i] != table2[i]:
                return False
        return True

