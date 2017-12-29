#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii
#
# algorithms
# Medium (32.72%)
# Total Accepted:    103.5K
# Total Submissions: 316.3K
# Testcase Example:  '[]\n5'
#
#
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
#
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Write a function to determine if a given target is in the array.
#
# The array may contain duplicates.
#


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums)==0:
            return False
        pivot = self.getPivot(nums)
        if self.binarySearch(nums, 0, pivot, target):
            return True
        else:
            return self.binarySearch(nums, pivot, len(nums) - 1, target)

    def binarySearch(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

    def getPivot(self, nums):
        for i in xrange(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i + 1
        return 0
