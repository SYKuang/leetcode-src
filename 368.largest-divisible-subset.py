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
        def factor(num):
            res = set()
            for i in xrange(1,int(num**0.5)+1):
                if num % i == 0:
                    res.add(i)
                    res.add(num/i)
            res.discard(num)
            return res
        if not nums:
            return []
        nums.sort()
        dp = {nums[0]:[nums[0]]}
        mx = -1
        res_index = nums[0]
        for i in xrange(1,len(nums)):
            dp[nums[i]]=[nums[i]]
            for f in factor(nums[i]):
                if f in nums and len(dp[nums[i]]) < len(dp[f])+1:
                    dp[nums[i]] = dp[f]+[nums[i]]
                    if len(dp[nums[i]]) > len(dp[res_index]):
                        res_index = nums[i]
        return dp[res_index]
