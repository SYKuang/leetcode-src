#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (34.71%)
# Total Accepted:    113.1K
# Total Submissions: 323.5K
# Testcase Example:  '"aab"'
#
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
#
# Return all possible palindrome partitioning of s.
#
#
# For example, given s = "aab",
#
# Return
#
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
#
#


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        isPal = [[False for _ in xrange(len(s))] for _ in xrange(len(s))]
        for i in xrange(len(s) - 1, -1, -1):
            for j in xrange(i, len(s)):
                if (i + 1 >= j - 1 or isPal[i + 1][j - 1]) and s[i] == s[j]:
                    isPal[i][j] = True
        self.ret = []
        self.sol = []
        self.findPartition(s, 0, isPal)
        return self.ret

    def findPartition(self, s, start, isPal):
        if start == len(s):
            self.ret.append(self.sol[:])
        for i in xrange(start, len(s)):
            if isPal[start][i]:
                self.sol.append(s[start:i + 1])
                self.findPartition(s, i + 1, isPal)
                self.sol.pop()
