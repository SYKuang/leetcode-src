#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii
#
# algorithms
# Medium (36.80%)
# Total Accepted:    127.7K
# Total Submissions: 344.3K
# Testcase Example:  '[1,2,2]'
#
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
#
# For example,
# If nums = [1,2,2], a solution is:
#
#
#
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
        return self.helper(sorted(nums),0)
    def helper(self,nums,index):
        if index==len(nums)-1:
            return [[],[nums[-1]]]
        else:
            ret = self.helper(nums,index+1)
            l = len(ret)
            for i in xrange(l):
                tmp=[nums[index]]+ret[i]
                if tmp not in ret:
                    ret.append(tmp)
            return ret
