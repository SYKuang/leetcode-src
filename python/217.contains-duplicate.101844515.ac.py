#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate
#
# Easy (44.87%)
# Total Accepted:    157873
# Total Submissions: 349802
# Testcase Example:  '[]'
#
# 
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
# 
#
class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = dict()
        for i in range(len(nums)):
            if nums[i] in table:
                return True
            table[nums[i]] = 1
        return False

