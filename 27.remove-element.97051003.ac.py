#
# [27] Remove Element
#
# https://leetcode.com/problems/remove-element
#
# Easy (38.11%)
# Total Accepted:    194955
# Total Submissions: 508129
# Testcase Example:  '[3,2,2,3]\n3'
#
# Given an array and a value, remove all instances of that value in place and
# return the new length.
# 
# 
# Do not allocate extra space for another array, you must do this in place with
# constant memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.
# 
# 
# Example:
# Given input array nums = [3,2,2,3], val = 3
# 
# 
# Your function should return length = 2, with the first two elements of nums
# being 2.
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        newTail=0
        for i in xrange(len(nums)):
            if nums[i]!=val:
                nums[newTail]=nums[i]
                newTail+=1
        return newTail
