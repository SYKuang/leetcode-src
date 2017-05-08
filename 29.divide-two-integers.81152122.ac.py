#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers
#
# Medium (15.96%)
# Total Accepted:    100573
# Total Submissions: 629766
# Testcase Example:  '0\n1'
#
# 
# Divide two integers without using multiplication, division and mod
# operator.
# 
# 
# If it is overflow, return MAX_INT.
# 
#
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647

        if divisor == 1:
            return dividend
        if divisor == 0:
            return  INT_MAX  
        a,b = abs(dividend), abs(divisor)
        neg = ( dividend > 0 and divisor < 0) or ( dividend < 0 and divisor >0)
      
        ans , shift = 0, 31
        while shift >= 0 :
            if a >= b << shift:
                a -= b << shift
                ans += 1 <<shift
            shift -= 1
        if neg:
            ans = -ans
        if ans > INT_MAX:
            return INT_MAX
        return ans
        
