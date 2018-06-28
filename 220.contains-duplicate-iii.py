#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (18.75%)
# Total Accepted:    70.5K
# Total Submissions: 375.5K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
#
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
#
#
#
# Example 3:
#
#
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
#
#
#
#
#
#


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        table = collections.OrderedDict()
        for i, n in enumerate(nums):
            key = n//max(1,t)
            for m in (key, key+1, key-1):
                if m in table and abs(n-table[m]) <= t:
                    print n,table[m]
                    return True
            table[key] = n
            if i>=k:
                table.popitem(last=False)
        return False
