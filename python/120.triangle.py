#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (34.54%)
# Total Accepted:    122K
# Total Submissions: 353.3K
# Testcase Example:  '[[-10]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
#
# For example, given the following triangle
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
#
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        n = len(triangle)
        # Define 65536 as max number
        dp = [[65536 for _ in xrange(n + 1)]for _ in xrange(n + 1)]
        for i, v in enumerate(triangle[-1]):
            dp[1][i + 1] = v
        for i in xrange(2, n + 1):
            for j in xrange(len(triangle[n - i])):
                dp[i][j + 1] = min(dp[i - 1][j + 1], dp[i - 1]
                                   [j + 2]) + triangle[n - i][j]
        return dp[n][1]
