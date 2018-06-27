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
        find = False
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                find = True
                break
        if not find:
            nums[:] = nums[::-1]
            return
        k = i+1
        for j in xrange(i+1, len(nums)):
            if nums[j] > nums[i] and nums[j] <= nums[k]:
                k = j

        nums[i], nums[k] = nums[k], nums[i]
        nums[i+1:] = reversed(nums[i+1:])
        return
