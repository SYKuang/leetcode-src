#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum
#
# Medium (38.12%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '[[0]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#


class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            if i == 0:
                dp[i][0] = grid[i][0]
            else:
                dp[i][0] = grid[i][0] + dp[i - 1][0]
        for i in xrange(n):
            if i == 0:
                dp[0][i] = grid[0][i]
            else:
                dp[0][i] = grid[0][i] + dp[0][i - 1]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]
