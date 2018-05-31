#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (37.88%)
# Total Accepted:    113.3K
# Total Submissions: 299K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
#


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [sys.maxint]*(n+1)
        dp[0] = 0
        for i in xrange(n+1):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i-j**2]+1, dp[i])
                j += 1
        return dp[n]
