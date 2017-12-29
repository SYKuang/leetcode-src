#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii
#
# Medium (31.73%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '[[0]]'
#
# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
# ⁠ [0,0,0],
# ⁠ [0,1,0],
# ⁠ [0,0,0]
# ]
#
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.
#


class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if 1 == obstacleGrid[0][0]:
            return 0

        dp = [1 for _ in xrange(len(obstacleGrid[0]))]
        for y in xrange(1, len(obstacleGrid[0])):
            if obstacleGrid[0][y] == 1:
                dp[y] = 0
            else:
                dp[y] = dp[y - 1]
        for x in xrange(1, len(obstacleGrid)):
            if obstacleGrid[x][0] == 1:
                dp[0] = 0
            for y in xrange(1, len(obstacleGrid[x])):
                if obstacleGrid[x][y] == 1:
                    dp[y] = 0
                else:
                    dp[y] = dp[y] + dp[y - 1]
        return dp[-1]
