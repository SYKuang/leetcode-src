#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
#
# algorithms
# Medium (36.29%)
# Total Accepted:    132.1K
# Total Submissions: 363.1K
# Testcase Example:  '[]'
#
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
#
# Your function should return length = 5, with the first five elements of nums
# being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new
# length.
#
#


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = 0
        for i, v in enumerate(nums):
            if end > 1:
                if v == nums[end - 2]:
                    continue
            nums[end] = v
            end = end + 1
        return end
