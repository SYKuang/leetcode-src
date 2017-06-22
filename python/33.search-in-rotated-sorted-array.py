#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array
#
# Medium (32.13%)
# Total Accepted:    167864
# Total Submissions: 522383
# Testcase Example:  '[]\n5'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        pivot = self.getPivot(nums)

        idx = self.binarySearch(nums, 0, pivot, target)
        if idx == -1:
            idx = self.binarySearch(nums, pivot, len(nums) - 1, target)
            return idx
        else:
            return idx

    def binarySearch(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def getPivot(self, nums):
        for i in xrange(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return i
        return 0
