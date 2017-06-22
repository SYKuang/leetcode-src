#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game
#
# Medium (29.42%)
# Total Accepted:    121323
# Total Submissions: 412355
# Testcase Example:  '[2,3,1,1,4]'
#
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
#
# Each element in the array represents your maximum jump length at that
# position.
#
#
# Determine if you are able to reach the last index.
#
#
#
# For example:
# A = [2,3,1,1,4], return true.
#
#
# A = [3,2,1,0,4], return false.
#
#


class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        maxPos = 0
        for i in xrange(len(nums) - 1):
            if i > maxPos:
                return False
            maxPos = max(maxPos, nums[i] + i)
        if maxPos >= len(nums) - 1:
            return True
        else:
            return False
