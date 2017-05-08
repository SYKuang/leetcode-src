#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes
#
# Easy (35.53%)
# Total Accepted:    91166
# Total Submissions: 255891
# Testcase Example:  '0'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        count = 5
        while count <= n:
            ret = ret + (n / count)
            count = count * 5
        return ret

