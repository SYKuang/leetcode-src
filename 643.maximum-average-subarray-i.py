#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (37.74%)
# Total Accepted:    30.4K
# Total Submissions: 80.6K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
#
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
#
#
# Example 1:
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
#
#
#
# Note:
#
# 1 k n
# Elements of the given array will be in the range [-10,000, 10,000].
#
#
#


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        start = 0
        res = -sys.maxint
        prev = 0.0
        end = 0
        while end < len(nums):
            prev += nums[end]
            if end - start == k-1:
                res = max(res, 1.0*prev/k)
                prev -= nums[start]
                start += 1
            end += 1
        return res
