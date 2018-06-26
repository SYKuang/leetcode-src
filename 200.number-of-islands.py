#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (37.17%)
# Total Accepted:    187.8K
# Total Submissions: 504.8K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
#
#


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])

        def dfs(x, y):
            if (x, y) in visited:
                return
            visited.add((x, y))
            for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= nx < m and 0 <= ny < n and not (nx, ny) in visited and grid[nx][ny] == "1":
                    dfs(nx, ny)

        res = 0
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == "1" and (x,y) not in visited:
                    res += 1
                    dfs(x, y)
        return res
