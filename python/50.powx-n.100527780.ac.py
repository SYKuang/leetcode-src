#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n
#
# Medium (26.65%)
# Total Accepted:    149185
# Total Submissions: 561942
# Testcase Example:  '8.88023\n3'
#
# Implement pow(x, n).
# 
#
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        import math
        return math.pow(x, n)
    def Power(self,x,n):
        if n==0:
            return 1

        half=self.Power(x,n/2)
        if n%2==1:
            return half*half*x
        else:
            return half*half
