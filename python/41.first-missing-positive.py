#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive
#
# Hard (25.53%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '[]'
#
#
# Given an unsorted integer array, find the first missing positive integer.
#
#
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
#
#
# Your algorithm should run in O(n) time and uses constant space.
#
#


class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        i = 0
        while i < len(nums):
            if nums[i] >= 1 and nums[i] <= len(nums) and nums[i] != (
                    i + 1) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i = i + 1
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums)+1
