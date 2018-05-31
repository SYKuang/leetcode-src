#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (37.26%)
# Total Accepted:    68K
# Total Submissions: 182.6K
# Testcase Example:  '[[]]'
#
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
#
#
#
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
#
#
#
#
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
#
#
#
#
# Write a function to compute the next state (after one update) of the board
# given its current state.
#
#
# Follow up:
#
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # define live_to_dead=2
        #        dead_to_live=3
        self.m = len(board)
        if not self.m:
            return
        self.n = len(board[0])
        self.board = board
        for x in xrange(self.m):
            for y in xrange(self.n):
                c = self.count(x, y)
                if self.board[x][y]:
                    if c > 3 or c < 2:
                        self.board[x][y] = 2
                else:
                    if c == 3:
                        self.board[x][y] = 3
        for x in xrange(self.m):
            for y in xrange(self.n):
                self.board[x][y] = self.board[x][y] % 2

    def count(self, x, y):
        count = 0
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                if 0 <= x+i < self.m and 0 <= y+j < self.n and not (i == 0 and j == 0) and (self.board[x+i][y+j] == 1 or self.board[x+i][y+j] == 2):
                    count += 1
        return count
