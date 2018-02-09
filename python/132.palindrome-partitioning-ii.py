#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (24.69%)
# Total Accepted:    78.3K
# Total Submissions: 317.4K
# Testcase Example:  '"aab"'
#
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using
# 1 cut.
#
#
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        isPal = [[False for _ in xrange(len(s))] for _ in xrange(len(s))]
        for i in xrange(len(s) - 1, -1, -1):
            for j in xrange(i, len(s)):
                if (i + 1 >= j - 1 or isPal[i + 1][j - 1]) and s[i] == s[j]:
                    isPal[i][j] = True

        dp=[65536 for _ in xrange(len(s)+1)]
        dp[0]=-1
        for i in xrange(1,len(s)+1):
            for j in xrange(i-1,-1,-1):
                if isPal[j][i-1]:
                    dp[i]=min(dp[i],dp[j]+1)
        return dp[len(s)]
