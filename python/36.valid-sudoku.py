#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku
#
# Medium (34.89%)
# Total Accepted:    116818
# Total Submissions: 332913
# Testcase Example:  '[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]'
#
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
#
#
#
# A partially filled sudoku which is valid.
#
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the
# filled cells need to be validated.
#
#


class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        table = [[[] for _ in xrange(9)] for _ in xrange(9)]
        for x in xrange(9):
            for y in xrange(9):
                if board[x][y] != ".":
                    table[x][y]=[int(board[x][y])]
                else:
                    table[x][y]=[i for i in xrange(1,10)]


        for x in xrange(9):

