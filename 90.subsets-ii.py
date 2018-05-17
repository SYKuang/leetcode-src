#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (38.56%)
# Total Accepted:    148K
# Total Submissions: 383.6K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rets = []
        l = len(nums)
        table=set()
        nums.sort()
        for n in xrange(2**l):
            ret = []
            i = 0
            while n:
                if n % 2:

                    ret.append(nums[i])
                n = n >> 1
                i+=1
            if tuple(ret) not in table:
                rets.append(ret)
                table.add(tuple(ret))
        return rets
