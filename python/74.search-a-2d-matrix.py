#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix
#
# algorithms
# Medium (34.90%)
# Total Accepted:    136.3K
# Total Submissions: 390.6K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
#
#
# For example,
#
# Consider the following matrix:
#
#
# [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
#
#
# Given target = 3, return true.
#


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        idxX, idxY = 0, len(matrix[0])-1
        lastX, lastY = 0, 0
        while idxX >= 0 and idxX < len(matrix) and idxY >= 0 and idxY < len(matrix[0]):
            if target == matrix[idxX][idxY]:
                return True
            elif target > matrix[idxX][idxY]:
                idxX = idxX + 1
            else:
                idxY = idxY - 1
        return False
