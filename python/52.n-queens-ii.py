#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii
#
# Hard (45.06%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '1'
#
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of
# distinct solutions.
#
#
#


class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ret = 0
        cols = []
        self.backtracking(n, 0, cols)
        return self.ret

    ##
    # @brief Check position is safe or not.
    #
    # @param n Total number of queen
    # @param row Current row
    # @param col Current column
    # @param cols Total column
    #
    # @return True if position is safe
    def isSafe(self, n, row, col, cols):
        for i in xrange(len(cols)):
            if cols[i] == col:
                return False
            if abs(row - i) == abs(col - cols[i]):
                return False
        return True

    ##
    # @brief backtracking function of N queens
    #
    # @param n Total number of queens
    # @param row Current row
    # @param cols Total column table
    #
    # @return
    def backtracking(self, n, row, cols):
        if n == row:
            self.ret = self.ret + 1
        for i in xrange(n):
            if self.isSafe(n, row, i, cols):
                cols.append(i)
                self.backtracking(n, row + 1, cols)
                cols.pop()
