#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (48.06%)
# Total Accepted:    28.7K
# Total Submissions: 59.8K
# Testcase Example:  '[1,2,1]'
#
#
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
#
#
# Example 1:
#
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
#
#
#
# Note:
# The length of given array won't exceed 10000.
#
#


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leng = len(nums)
        if not leng:
            return []
        max_idx = 0
        max_num = nums[0]
        for i in xrange(1, leng):
            if nums[i] > max_num:
                max_num = nums[i]
                max_idx = i
        stack = [max_num]
        idx = (max_idx - 1) % leng
        res = [-1]*leng
        while idx != max_idx:
            n = nums[idx]
            while stack and stack[-1] <= n:
                stack.pop()
            if stack:
                res[idx] = stack[-1]
            stack.append(n)
            idx = (idx-1) % leng
        return res


class Solution2(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums)
        stack = []
        leng = len(nums)
        nums = nums*2
        for i, n in enumerate(nums):
            while stack and stack[-1][0] < n:
                _, index = stack.pop()
                res[index] = n
            if i < leng:
                stack.append((n, i))
        return res
