#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.12%)
# Total Accepted:    153.8K
# Total Submissions: 528.2K
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
        l=len(nums)
        i=l-2
        # Find first increasing order number
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i<0:
            nums[:]=nums[::-1]
        else:
            j=i+1
            # Find last decreasing order number
            while j<l and nums[j]>nums[i]:
                j+=1
            j-=1
            # Swap i,j
            nums[i],nums[j]=nums[j],nums[i]
            nums[i+1:]=sorted(nums[i+1:])
