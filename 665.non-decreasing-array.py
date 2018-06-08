#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (20.06%)
# Total Accepted:    26.5K
# Total Submissions: 132.1K
# Testcase Example:  '[4,2,3]'
#
#
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
#
#
#
# We define an array is non-decreasing if array[i]  holds for every i (1
#
# Example 1:
#
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
#
#
#
# Example 2:
#
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
#
#
#
# Note:
# The n belongs to [1, 10,000].
#
#


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 1
        for i in xrange(1, len(nums)):
            if nums[i] < nums[i-1]:
                if not count:
                    return False
                if i == 1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                count -= 1
        return True
