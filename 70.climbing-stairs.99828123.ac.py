#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs
#
# Easy (39.36%)
# Total Accepted:    171649
# Total Submissions: 434337
# Testcase Example:  '1'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Note: Given n will be a positive integer.
# 
#
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n ==1:
            return 1
        elif n ==2:
            return 2
        retArr=[0,1,2]
        for i in range(3,n+1):
            retArr.append(retArr[i-1]+retArr[i-2])
        return retArr[n]
        
    
