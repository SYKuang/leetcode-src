#
# [351] Android Unlock Patterns
#
# https://leetcode.com/problems/android-unlock-patterns/description/
#
# algorithms
# Medium (44.56%)
# Total Accepted:    21.6K
# Total Submissions: 48.5K
# Testcase Example:  '1\n1'
#
#
# Given an Android 3x3 key lock screen and two integers m and n, where  1 ≤ m ≤
# n ≤ 9, count the total number of unlock patterns of the Android lock screen,
# which consist of minimum of m keys and maximum n keys.
#
# Rules for a valid pattern:
#
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any
# other keys, the other keys must have previously selected in the pattern. No
# jumps through non selected key is allowed.
# The order of keys used matters.
#
#
#
#
#
# Explanation:
#
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
#
#
#
# Invalid move: 4 - 1 - 3 - 6
#
# Line  1 - 3 passes through key 2 which had not been selected in the pattern.
#
# Invalid move: 4 - 1 - 9 - 2
#
# Line  1 - 9 passes through key 5 which had not been selected in the pattern.
#
# Valid move: 2 - 4 - 1 - 3 - 6
#
# Line 1 - 3 is valid because it passes through key 2, which had been selected
# in the pattern
#
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
#
# Line 1 - 9 is valid because it passes through key 5, which had been selected
# in the pattern.
#
# Example:
# Given m = 1, n = 1, return 9.
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = {}
        skip[(1, 3)] = 2
        skip[(1, 7)] = 4
        skip[(1, 9)] = 5
        skip[(2, 8)] = 5
        skip[(3, 7)] = 5
        skip[(3, 9)] = 6
        skip[(4, 6)] = 5
        skip[(7, 9)] = 8
        self.res = 0

        def bfs(used, start):
            if len(used) >= m:
                self.res += 1
            if len(used) == n:
                return
            for j in xrange(1, 10):
                if j in used:
                    continue
                edge = (min(j, start), max(j, start))
                if edge not in skip or skip[edge] in used:
                    bfs(used+[j], j)
        res = 0
        bfs([1], 1)
        res += self.res*4
        self.res = 0
        bfs([5], 5)
        res += self.res
        self.res = 0
        bfs([2], 2)
        res += self.res*4
        return res
