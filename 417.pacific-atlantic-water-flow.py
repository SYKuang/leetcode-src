#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (35.02%)
# Total Accepted:    28K
# Total Submissions: 79.7K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
#
# Note:
#
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
#
#
# Example:
#
# Given the following 5x5 matrix:
#
# ⁠ Pacific ~   ~   ~   ~   ~
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
#
#
#


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        Pacific = [[False] * n for _ in xrange(m)]
        q = collections.deque()
        for i in xrange(n):
            q.append((0, i))
            Pacific[0][i] = True
        for i in xrange(1, m):
            q.append((i, 0))
            Pacific[i][0] = True
        while q:
            x, y = q.popleft()
            for nx, ny in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] >= matrix[x][y] and not Pacific[nx][ny]:
                    Pacific[nx][ny] = True
                    q.append((nx, ny))
        res = []
        q = collections.deque()
        Atlantic = [[False] * n for _ in xrange(m)]

        for i in xrange(n):
            q.append((m-1, i))
            Atlantic[m-1][i] = True
        for i in xrange(m):
            q.append((i, n-1))
            Atlantic[i][n-1] = True
        while q:
            x, y = q.popleft()
            for nx, ny in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] >= matrix[x][y] and not Atlantic[nx][ny]:
                    Atlantic[nx][ny] = True
                    q.append((nx, ny))
        for x in xrange(m):
            for y in xrange(n):
                if Atlantic[x][y] and Pacific[x][y]:
                    res.append([x, y])
        return res
