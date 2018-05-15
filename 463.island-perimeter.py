#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (58.07%)
# Total Accepted:    81.2K
# Total Submissions: 139.7K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water. Grid cells are connected
# horizontally/vertically (not diagonally). The grid is completely surrounded
# by water, and there is exactly one island (i.e., one or more connected land
# cells). The island doesn't have "lakes" (water inside that isn't connected to
# the water around the island). One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
#
# Example:
#
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
#
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:
#
#
#
#


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y]==1:
                    for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                        if nx >= m or ny >= n or nx < 0 or ny < 0 or grid[nx][ny] == 0:
                            ret += 1
        return ret
