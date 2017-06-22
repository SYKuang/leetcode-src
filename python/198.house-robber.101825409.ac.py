#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber
#
# Easy (38.23%)
# Total Accepted:    132746
# Total Submissions: 345441
# Testcase Example:  '[]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases. Also thanks to @ts for adding additional test cases.
#
class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        robbed = []
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        robbed.append(nums[0])
        robbed.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            robbed.append(max(robbed[i - 1], robbed[i - 2] + nums[i]))
        return robbed[-1]

