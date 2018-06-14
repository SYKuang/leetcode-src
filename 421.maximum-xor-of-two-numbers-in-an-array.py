#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (48.14%)
# Total Accepted:    23.6K
# Total Submissions: 49K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 231.
#
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
#
# Could you do this in O(n) runtime?
#
# Example:
#
# Input: [3, 10, 5, 25, 2, 8]
#
# Output: 28
#
# Explanation: The maximum result is 5 ^ 25 = 28.
#
#
#


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        mask = 0
        for i in xrange(31, -1, -1):
            mask = mask | (1 << i)
            s = set()
            for n in nums:
                s.add(n & mask)
            tmp = res | (1 << i)
            for n in s:
                if (n ^ tmp) in s:
                    res = tmp
                    break
        return res
