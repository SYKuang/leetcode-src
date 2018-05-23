#
# [360] Sort Transformed Array
#
# https://leetcode.com/problems/sort-transformed-array/description/
#
# algorithms
# Medium (44.97%)
# Total Accepted:    17.8K
# Total Submissions: 39.6K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
#
# Given a sorted array of integers nums and integer values a, b and c.  Apply a
# quadratic function of the form f(x) = ax2 + bx + c to each element x in the
# array.
#
# The returned array must be in sorted order.
#
# Expected time complexity: O(n)
#
# Example:
#
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
#
# Result: [3, 9, 15, 33]
#
# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
#
# Result: [-23, -5, 1, 7]
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def transform(x, a, b, c):
            return a*(x ** 2)+b*x+c

        if a == 0:
            if b > 0:
                return [transform(x,a,b,c) for x in nums]
            elif b < 0:
                return [transform(x,a,b,c) for x in nums[::-1]]
            else:
                return [c]*len(nums)

        ret = []
        start = 0
        end = len(nums)-1

        if a > 0:
            while start <= end:
                e = transform(nums[end], a, b, c)
                s = transform(nums[start], a, b, c)
                if e > s:
                    ret.append(e)
                    end -= 1
                else:
                    ret.append(s)
                    start += 1
            return ret[::-1]
        else:
            while start <= end:
                e = transform(nums[end], a, b, c)
                s = transform(nums[start], a, b, c)
                if e < s:
                    ret.append(e)
                    end -= 1
                else:
                    ret.append(s)
                    start += 1
            return ret
