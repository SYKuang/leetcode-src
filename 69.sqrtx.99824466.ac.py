#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx
#
# Easy (27.46%)
# Total Accepted:    152440
# Total Submissions: 553204
# Testcase Example:  '0'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start ,end = 1 ,x
        while start+1 < end:
            mid=(start+end)/2
            midSquare = mid*mid
            if midSquare == x:
                return mid
            elif midSquare < x:
                start = mid
            else:
                end = mid
        if end*end <= x:
            return end
        else:
            return start
            
