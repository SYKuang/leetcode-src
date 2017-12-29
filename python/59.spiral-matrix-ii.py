#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii
#
# Medium (39.14%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '0'
#
# Given an integer n, generate a square matrix filled with elements from 1 to
# n2 in spiral order.
#
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
#
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret=[[0 for _ in xrange(n)] for _ in xrange(n)]
        # 0: go right
        # 1: go down
        # 2: go up
        #
        row,col=0,0
        val=1
        for i in xrange(n/2):
            last=n-1-i
            for j in xrange(i,last):
                ret[i][j]=val
                val=val+1
            for j in xrange(i,last):
                ret[j][last]=val
                val=val+1
            for j in xrange(last,i,-1):
                ret[last][j]=val
                val=val+1
            for j in xrange(last,i,-1):
                ret[j][i]=val
                val=val+1
        if n%2==1:
            ret[n/2][n/2]=n*n
        return ret
