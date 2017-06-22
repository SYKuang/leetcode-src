#
# [34] Search for a Range
#
# https://leetcode.com/problems/search-for-a-range
#
# Medium (31.14%)
# Total Accepted:    133777
# Total Submissions: 428780
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers sorted in ascending order, find the starting and
# ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
#
#


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        idx = self.binarySearch(nums, target)
        if idx == -1:
            return [-1, -1]
        else:
            start = idx
            while start >= 0:
                if nums[start] != target:
                    start = start + 1
                    break
                start -= 1

            if start == -1:
                start = 0
            end = idx
            while end < len(nums):
                if nums[end] != target:
                    end = end - 1
                    break
                end += 1
            if end == len(nums):
                end = len(nums) - 1
            return [start, end]

    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
