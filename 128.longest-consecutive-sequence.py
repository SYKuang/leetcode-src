#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (38.62%)
# Total Accepted:    147.4K
# Total Submissions: 381.4K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
#


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets = set(nums)
        res = 0
        while sets:
            keys = list(sets)
            sets.remove(keys[0])
            k = keys[0]+1
            lens = 1
            while k in sets:
                lens += 1
                sets.remove(k)
                k += 1
            k = keys[0]-1
            while k in sets:
                lens += 1
                sets.remove(k)
                k -= 1
            res = max(res, lens)
        return res
