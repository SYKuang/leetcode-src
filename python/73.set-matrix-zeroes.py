#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes
#
# Medium (35.98%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '[[0]]'
#
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in place.
#
#
# click to show follow up.
#
# Follow up:
#
#
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
#
#
#


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        x_zero = [0 for _ in xrange(len(matrix))]
        y_zero = [0 for _ in xrange(len(matrix[0]))]
        for x in xrange(len(matrix)):
            for y in xrange(len(matrix[0])):
                if matrix[x][y] == 0:
                    x_zero[x] = 1
                    y_zero[y] = 1
        for x in xrange(len(x_zero)):
            if x_zero[x]==1:
                for y in xrange(len(matrix[0])):
                    matrix[x][y]=0
        for y in xrange(len(y_zero)):
            if y_zero[y]==1:
                for x in xrange(len(matrix)):
                    matrix[x][y]=0
