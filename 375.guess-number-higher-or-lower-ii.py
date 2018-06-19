#
# [375] Guess Number Higher or Lower II
#
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
#
# algorithms
# Medium (36.22%)
# Total Accepted:    31.9K
# Total Submissions: 88.1K
# Testcase Example:  '1'
#
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number I picked is
# higher or lower.
#
# However, when you guess a particular number x,  and you guess wrong, you pay
# $x. You win the game when you guess the number I picked.
#
#
# Example:
#
# n = 10, I pick 8.
#
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
#
# Game over. 8 is the number I picked.
#
# You end up paying $5 + $7 + $9 = $21.
#
#
#
# Given a particular n ≥ 1, find out how much money you need to have to
# guarantee a win.
#
# Credits:Special thanks to @agave and @StefanPochmann for adding this problem
# and creating all test cases.
#


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in xrange(n+1)]
        for i in xrange(2, n+1):
            for j in xrange(i-1, 0, -1):
                global_min = sys.maxint
                for k in xrange(j+1, i):
                    local_mx = k+max(dp[j][k-1], dp[k+1][i])
                    global_min = min(global_min, local_mx)
                dp[j][i] = j if j == i-1 else global_min
        return dp[1][n]
