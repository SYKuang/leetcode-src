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
        left=0
        zero=0
        k=1
        res=0
        for right in xrange(len(nums)):
            if not nums[right]:
                zero+=1
            while zero>k:
                if not nums[left]:
                    zero-=1
                left+=1
            res=max(res,right-left+1)
        return res
