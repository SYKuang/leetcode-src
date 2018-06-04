#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
#
# algorithms
# Medium (45.51%)
# Total Accepted:    14.2K
# Total Submissions: 31.2K
# Testcase Example:  '[1,0,1,1,0,1]'
#
#
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.
#
#
# Example 1:
#
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of
# consecutive 1s.
# ⁠   After flipping, the maximum number of consecutive 1s is 4.
#
#
#
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
#
#
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other
# words, you can't store all numbers coming from the stream as it's too large
# to hold in memory. Could you solve it efficiently?
#
#


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = []
        right = []
        count = 0
        for i, n in enumerate(nums):
            left.append(count)
            if n:
                count += 1
            else:
                count = 0
        count = 0
        for i, n in enumerate(nums[::-1]):
            right.append(count)
            if n:
                count += 1
            else:
                count = 0
        right=right[::-1]
        res = -1
        for i in xrange(len(nums)):
            if not nums[i]:
                res = max(res, left[i]+right[i]+1)
        return len(nums) if res < 0 else res
