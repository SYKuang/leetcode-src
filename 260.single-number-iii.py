#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (53.70%)
# Total Accepted:    84.8K
# Total Submissions: 157.9K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
#
# Example:
#
#
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
#
# Note:
#
#
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
#
#
#


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Very tricky
        # First, we find the one bit which is different between res1 and res2.
        # Because res1 and res2 are different two nums, there must at least
        # exist one bit is different.

        xor = 0
        for n in nums:
            xor ^= n
        mask = 1
        while (xor & mask) == 0:
            mask = mask << 1
        # Second, we use the mask to do xor. In the other word, we use the bit
        # to distinguish nums to 2 group, one with the bit and the other group
        # is nums without the bit.
        # And then we do the xor again. We can find out two nums by doing xor.
        res = [0, 0]
        for n in nums:
            if n & mask:
                res[1] ^= n
            else:
                res[0] ^= n
        return res
