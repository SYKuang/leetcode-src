#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (29.03%)
# Total Accepted:    235.7K
# Total Submissions: 811.5K
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
#
# Example 1:
#
#
# Input: 4
# Output: 2
#
#
# Example 2:
#
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
# the decimal part is truncated, 2 is returned.
#
#
#


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Use Newton's method to get sqrt;
        # To get sqrt of n, it equals to find answer of f(x)=x^2 -n
        # According Newton's method, the x1,x2,x3.... will reach the answer.
        # x1=x0+f(x0)/f'(x0)
        if x==0:
            return 0
        ret = 1.0
        pre = 0.0
        # When ret equals to pre means we get the answer
        while ret != pre:
            pre = ret
            ret = (ret+x/ret)/2
        return int(ret)
