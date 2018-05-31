#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (51.14%)
# Total Accepted:    92K
# Total Submissions: 179.9K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
#
#
#


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        return [i for i in xrange(1, len(nums)+1) if i not in s]
        # l = len(nums)
        # i = 0
        # while i < l:
        # if nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
        # nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        # else:
        # i += 1
        # res = []
        # for i, n in enumerate(nums):
        # if n != i+1:
        # res.append(i+1)
        # return res
