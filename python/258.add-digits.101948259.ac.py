#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits
#
# Easy (50.73%)
# Total Accepted:    161478
# Total Submissions: 317454
# Testcase Example:  '0'
#
# 
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit. 
# 
# 
# 
# For example:
# 
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
# one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        return (num - 1) % 9 + 1

