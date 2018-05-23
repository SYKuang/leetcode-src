#
# [562] Longest Line of Consecutive One in Matrix
#
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/
#
# algorithms
# Medium (41.21%)
# Total Accepted:    7.4K
# Total Submissions: 17.9K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[0,0,0,1]]'
#
# Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal or anti-diagonal.
#
# Example:
#
# Input:
# [[0,1,1,0],
# ⁠[0,1,1,0],
# ⁠[0,0,0,1]]
# Output: 3
#
#
#
#
# Hint:
# The number of elements in the given matrix will not exceed 10,000.
#
#


class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.m = len(M)
        if not self.m:
            return 0
        self.n = len(M[0])
        ret = 0
        self.table={}
        self.M=M
        for x in xrange(self.m):
            for y in xrange(self.n):
                for direct in ((1, 0), (0, 1), (1, 1), (-1, 1)):
                    ret = max(ret, self.getLen(direct, x, y))
        return ret

    def getLen(self, direct, x, y):
        dx, dy = direct
        if (dx, dy, x, y) in self.table:
            return self.table[(dx, dy, x, y)]
        if x < 0 or x >= self.m or y < 0 or y >= self.n or self.M[x][y] == 0:
            return 0
        ret = 1+self.getLen(direct, x+dx, y+dy)
        self.table[(dx, dy, x, y)] = ret
        return ret
