#
# [78] Subsets
#
# https://leetcode.com/problems/subsets
#
# Medium (39.47%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '[1,2,3]'
#
#
# Given a set of distinct integers, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
#
# For example,
# If nums = [1,2,3], a solution is:
#
#
#


class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        rets = []
        rets.append([])
        nums.sort(reverse=True)
        for i in range(len(nums)):
            n = len(rets)
            for j in range(n):
                ret = list(rets[j])
                ret.insert(0, nums[i])
                rets.append(ret)
        return rets
