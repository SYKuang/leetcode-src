#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens
#
# Hard (31.23%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
#
#


class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        rets = []
        ret = []
        cols = []
        self.backtracking(n, 0, cols, ret, rets)
        return rets
    ##
    # @brief Backtracing for N queens
    #
    # @param n How many queens
    # @param row Current Row
    # @param cols Column table to record queen's position
    # @param ret Current Result
    # @param rets Total Results
    #
    # @return

    def backtracking(self, n, row, cols, ret, rets):
        if n == row:
            rets.append(list(ret))
        else:
            for i in xrange(n):
                if self.isSafe(row, i, cols):
                    sol = ['.' for _ in xrange(n)]
                    sol[i] = 'Q'
                    cols.append(i)
                    ret.append("".join(sol))
                    self.backtracking(n, row + 1, cols, ret, rets)
                    ret.pop()
                    cols.pop()

    ##
    # @brief Check position is safe to place or not
    #
    # @param row Row of position
    # @param col Column of position
    # @param cols Column table to record position of queen
    #
    # @return True if is safe else return False
    def isSafe(self, row, col, cols):
        for i in xrange(row):
            if col == cols[i]:
                return False
            if abs(row - i) == abs(col - cols[i]):
                return False
        return True
