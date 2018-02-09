#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (19.13%)
# Total Accepted:    95K
# Total Submissions: 494.5K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
#
#
# For example,
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
#
#
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
#


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        queue = []
        if len(board) == 0:
            return
        for y in xrange(len(board[0])):
            if board[0][y] == "O":
                queue.append((0, y))
            if board[-1][y] == "O":
                queue.append((len(board) - 1, y))
        for x in xrange(len(board)):
            if board[x][0] == "O":
                queue.append((x, 0))
            if board[x][-1] == "O":
                queue.append((x, len(board[0]) - 1))
        self.mark(queue, board)
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "Y":
                    board[x][y] = "O"

    def mark(self,  queue, board):
        while len(queue) > 0:
            x = queue[0][0]
            y = queue[0][1]
            board[x][y] = "Y"
            if x > 0:
                if board[x - 1][y] == "O":
                    queue.append((x - 1, y))
            if x < len(board) - 1:
                if board[x + 1][y] == "O":
                    queue.append((x + 1, y))
            if y > 0:
                if board[x][y - 1] == "O":
                    queue.append((x, y - 1))
            if y < len(board[0]) - 1:
                if board[x][y + 1] == "O":
                    queue.append((x, y + 1))
            del queue[0]
