#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (26.01%)
# Total Accepted:    136.1K
# Total Submissions: 522.9K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#
#

# Reference
# http://bangbingsyb.blogspot.tw/2014/11/leetcode-first-missing-positive.html


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # To avoid to use extra space, we try to make nums as a hash table which
        # nums[i]=i+1

        i = 0
        n = len(nums)
        while i < n:
            if 0 < nums[i] <= n and nums[i] != (i+1) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        for i in xrange(n):
            if nums[i] != i+1:
                return i+1
        return n+1
