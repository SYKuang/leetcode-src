#
# [46] Permutations
#
# https://leetcode.com/problems/permutations
#
# Medium (42.20%)
# Total Accepted:    163971
# Total Submissions: 383989
# Testcase Example:  '[1,2,3]'
#
#
# Given a collection of distinct numbers, return all possible permutations.
#
#
#
# For example,
# [1,2,3] have the following permutations:
#
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#
#


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.permuteRes(nums, 0, ret)
        return ret

    def permuteRes(self, nums, begin, ret):
        if begin >= len(nums):
            nums1 = list(nums)
            ret.append(nums1)
        else:
            for i in xrange(begin, len(nums)):
                nums[begin], nums[i] = nums[i], nums[begin]
                self.permuteRes(nums, begin + 1, ret)
                nums[begin], nums[i] = nums[i], nums[begin]
