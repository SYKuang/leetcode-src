#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix
#
# Medium (25.16%)
# Total Accepted:    93118
# Total Submissions: 370053
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# 
# 
# For example,
# Given the following matrix:
# 
# 
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# 
# You should return [1,2,3,6,9,8,7,4,5].
# 
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        Ret=[]
        while matrix:
            for i in matrix[0]:
                Ret.append(i)
            matrix= list(reversed(zip(*matrix[1:])))
            
        return Ret
