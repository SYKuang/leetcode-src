#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
#
# Easy (47.22%)
# Total Accepted:    75705
# Total Submissions: 160556
# Testcase Example:  '[2,3,4]\n6'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2. Please note that
# your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# 
#
class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) == 0:
            return None
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                left = left + 1
        return None

