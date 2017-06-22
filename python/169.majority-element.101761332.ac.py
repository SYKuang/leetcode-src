#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element
#
# Easy (45.82%)
# Total Accepted:    191422
# Total Submissions: 415696
# Testcase Example:  '[1]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        last = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == last:
                count = count + 1
                if count > len(nums)/2:
                    return nums[i]
            else:
                last = nums[i]
                count = 1
        return last

