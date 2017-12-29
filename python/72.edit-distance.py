#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance
#
# Hard (31.78%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '""\n""'
#
#
# Given two words word1 and word2, find the minimum number of steps required to
# convert word1 to word2. (each operation is counted as 1 step.)
#
#
#
# You have the following 3 operations permitted on a word:
#
#
#
# a) Insert a character
# b) Delete a character
# c) Replace a character
#
#


class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        table = [[0 for _ in xrange(len(word2) + 1)]
                 for _ in xrange(len(word1) + 1)]
        for i in xrange(len(word2) + 1):
            table[0][i] = i
        for i in xrange(len(word1) + 1):
            table[i][0] = i
        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                table[i][j] = min(table[i - 1][j] + 1,
                                  table[i][j - 1] + 1, table[i-1][j-1] + apply(lambda: 0 if word1[i-1] == word2[j-1] else 1))
        return table[-1][-1]
