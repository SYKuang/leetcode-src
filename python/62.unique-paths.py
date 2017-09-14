#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths
#
# Medium (40.57%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '1\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# How many possible unique paths are there?
#
#
#
# Above is a 3 x 7 grid. How many possible unique paths are there?
#
#
# Note: m and n will be at most 100.
#


class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ret = 1
        down = 1
        small = min(m - 1, n - 1)
        if small == 0:
            return 1
        for i in xrange(1, small+1):
            ret = ret * (m + n - 1 - i)
            down = down * i
        return ret/down
