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

# Uisng Lagrange's four-square theorem


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a**2 < n:
            b = int(math.sqrt(n-a**2))
            if a**2+b**2 == n:
                return int(not not a) + int(not not b)
            a += 1
        return 3
# Using DP


class Solution2(object):
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
