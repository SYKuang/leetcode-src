#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii
#
# Easy (31.97%)
# Total Accepted:    108459
# Total Submissions: 338205
# Testcase Example:  '[]\n0'
#
# 
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
#
class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = dict()
        for i in xrange(len(nums)):
            if nums[i] in table:
                return True
            table[nums[i]] = 1
            if i >= k:
                del table[nums[i - k]]
        return False

