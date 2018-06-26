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
            while i+j*j <= n:
                dp[i+j*j] = min(dp[i+j*j], dp[i]+1)
                j+=1
        return dp[n]


class Solution2(object):
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
        while a*a <= n:
            b = int(math.sqrt(n-a*a))
            if b*b+a*a == n:
                a = 1 if a else 0
                b = 1 if b else 0
                return a+b
            a += 1
        return 3
