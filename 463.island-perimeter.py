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
        if not grid:
            return 0
        res = 0

        for x in xrange(len(grid)):
            for y in xrange(len(grid[0])):
                if grid[x][y] == 0:
                    continue
                res += 4
                if x > 0 and grid[x-1][y] == 1:
                    res -= 2
                if y > 0 and grid[x][y-1] == 1:
                    res -= 2
        return res
