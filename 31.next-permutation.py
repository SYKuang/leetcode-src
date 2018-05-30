#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.10%)
# Total Accepted:    154.6K
# Total Submissions: 531.2K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i == -1:
            nums[:]=nums[::-1]
        else:
            j = i+1
            for k in xrange(j, len(nums)):
                if nums[k] > nums[i] and nums[k] <= nums[j]:
                    j = k
            nums[i], nums[j] = nums[j], nums[i]
            k=len(nums)
            nums[i+1:] = nums[:i:-1]
