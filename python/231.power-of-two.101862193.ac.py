#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two
#
# Easy (39.77%)
# Total Accepted:    132958
# Total Submissions: 333574
# Testcase Example:  '1'
#
# 
# Given an integer, write a function to determine if it is a power of two.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n % 2 > 0:
                return False
            n = n / 2
        if n == 1:
            return True
        else:
            return False

