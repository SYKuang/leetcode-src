#
# [79] Word Search
#
# https://leetcode.com/problems/word-search
#
# algorithms
# Medium (27.18%)
# Total Accepted:    144.2K
# Total Submissions: 530.5K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
#
# Given a 2D board and a word, find if the word exists in the grid.
#
#
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
#
# For example,
# Given board =
#
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
#
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
#
#


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0 or len(board) == 0:
            return False
        self.visited = [[False for _ in xrange(len(board[0]))]
                        for _ in xrange(len(board))]
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                if self.findword(board,word,x,y):
                    return True
        return False
    def findword(self, board, word, x, y):
        if len(word) == 0:
            return True
        if x == len(board) or x == -1 or y == len(
                board[0]) or y == -1 or self.visited[x][y] or word[0] != board[x][y]:
            return False
        self.visited[x][y] = True
        if self.findword(board, word[1:], x - 1, y):
            return True
        if self.findword(board, word[1:], x, y - 1):
            return True
        if self.findword(board, word[1:], x + 1, y):
            return True
        if self.findword(board, word[1:], x, y + 1):
            return True
        self.visited[x][y] = False
        return False
