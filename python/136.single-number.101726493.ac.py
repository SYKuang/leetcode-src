#
# [136] Single Number
#
# https://leetcode.com/problems/single-number
#
# Easy (53.72%)
# Total Accepted:    215719
# Total Submissions: 399892
# Testcase Example:  '[1]'
#
# Given an array of integers, every element appears twice except for one. Find
# that single one.
# 
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
#
class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            # Take advantage of XOR => x XOR x = 0, x XOR x XOR y = y
            ret = 0
            for i in nums:
                ret = ret ^ i
            return ret

