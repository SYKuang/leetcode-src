#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (33.93%)
# Total Accepted:    35.2K
# Total Submissions: 103.8K
# Testcase Example:  '[1,2,3]'
#
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj %
# Si = 0.
#
#
# If there are multiple solutions, return any subset is fine.
#
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
#
#
#
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]
#
#
#
# Credits:Special thanks to @Stomach_ache for adding this problem and creating
# all test cases.
#


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        dp = [[] for _ in xrange(len(nums))]
        parent = [-1]*len(nums)
        mx = -1
        index = -1
        for i in xrange(len(nums)):
            dp[i].append(nums[i])
            for j in xrange(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j])+1:
                    dp[i] = dp[j]+[nums[i]]
                    if len(dp[i]) > len(dp[index]):
                        index = i
        return dp[index]
