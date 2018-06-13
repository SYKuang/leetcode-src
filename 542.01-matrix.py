#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (33.06%)
# Total Accepted:    22.1K
# Total Submissions: 66.7K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
# Output:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
#
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
#
# Output:
#
# 0 0 0
# 0 1 0
# 1 2 1
#
#
#
# Note:
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#
#
#


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        q = []
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j]:
                    matrix[i][j] = sys.maxint-1
                else:
                    q.append((i, j))
        while q:
            newQ = []
            for i, j in q:
                z = matrix[i][j]+1
                for nI, nJ in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                    if 0 <= nI < m and 0 <= nJ < n and matrix[nI][nJ] > z:
                        matrix[nI][nJ] = z
                        newQ.append((nI, nJ))
            q = newQ
        return matrix


class Solution2(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        res = [[sys.maxint-1]*n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i-1][j]+1, res[i][j])
                    if j > 0:
                        res[i][j] = min(res[i][j-1]+1, res[i][j])
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if res[i][j] > 1:
                    if i < m-1:
                        res[i][j] = min(res[i+1][j]+1, res[i][j])
                    if j < n-1:
                        res[i][j] = min(res[i][j+1]+1, res[i][j])
        return res
