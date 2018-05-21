#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (38.94%)
# Total Accepted:    128.2K
# Total Submissions: 329.3K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
# Example:
#
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
# Note:
#
#
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
#


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #O(nlogn) Robinson-Schensted-Knuth Algorithm
        if len(nums) == 0:
            return 0
        dp = [nums[0]]

        for n in nums[1:]:
            if n > dp[-1]:
                dp.append(n)
            else:
                dp[bisect.bisect_left(dp, n)] = n
        return len(dp)

        """ O(n^2)
        if len(nums) == 0:
            return 0
        dp = [1]*len(nums)
        ret = 1
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        """
