#
# [308] Range Sum Query 2D - Mutable
#
# https://leetcode.com/problems/range-sum-query-2d-mutable/description/
#
# algorithms
# Hard (26.35%)
# Total Accepted:    23K
# Total Submissions: 87.4K
# Testcase Example:  '["NumMatrix","sumRegion","update","sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[3,2,2],[2,1,4,3]]'
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
#
#
#
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
# and (row2, col2) = (4, 3), which contains sum = 8.
#
#
# Example:
#
# Given matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
#
#
#
# Note:
#
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is
# distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
#
#
#


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m = len(matrix)
        self.n = len(matrix[0]) if self.m else 0
        self.matrix = matrix
        self.row = [[] for _ in xrange(self.m)]
        for i, row in enumerate(matrix):
            count = 0
            for n in row:
                count += n
                self.row[i].append(count)
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val-self.matrix[row][col]
        self.matrix[row][col] = val
        for j in xrange(col, self.n):
            self.row[row][j] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = 0
        for r in xrange(row1, min(row2+1, self.m)):
            ret += self.row[r][col2]
            ret -= self.row[r][col1-1] if col1 != 0 else 0
        return ret
# Your NumMatrix object will be instantiated and called as such:
    # obj = NumMatrix(matrix)
    # obj.update(row,col,val)
    # param_2 = obj.sumRegion(row1,col1,row2,col2)
