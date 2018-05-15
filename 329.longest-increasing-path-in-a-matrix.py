#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (37.48%)
# Total Accepted:    53.2K
# Total Submissions: 141.8K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
#
#
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
#
#
# Example 1:
#
# nums = [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ]
#
#
#
#
# Return 4
#
# The longest increasing path is [1, 2, 6, 9].
#
#
# Example 2:
#
# nums = [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ]
#
#
#
#
# Return 4
#
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not
# allowed.
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.m = len(matrix)
        if self.m == 0:
            return 0
        self.n = len(matrix[0])
        self.ret = 0
        self.matrix = matrix
        self.table = {}
        for x in xrange(self.m):
            for y in xrange(self.n):
                self.ret = max(self.dfs((x, y),  set()), self.ret)
        return self.ret

    def dfs(self, pos,  visited):
        if pos in self.table:
            return self.table[pos]
        x, y = pos
        visited.add((x, y))
        l = 0
        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= nx < self.m and 0 <= ny < self.n and (nx, ny) not in visited and self.matrix[nx][ny] > self.matrix[x][y]:
                l = max(self.dfs((nx, ny),  visited), l)
        visited.remove((x, y))
        self.table[pos] = 1+l
        return 1+l
