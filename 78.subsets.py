#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (45.29%)
# Total Accepted:    238.2K
# Total Submissions: 525.6K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rets = []
        l = len(nums)
        for n in xrange(2**l):
            ret = []
            i = 0
            while n:
                if n % 2:
                    ret.append(nums[i])
                n = n >> 1
                i+=1
            rets.append(ret)
        return rets
