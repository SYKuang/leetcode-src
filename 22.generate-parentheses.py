#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (48.65%)
# Total Accepted:    220.1K
# Total Submissions: 450.9K
# Testcase Example:  '3'
#
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in xrange(n+1)]
        dp[0] = [""]
        for i in xrange(1, n+1):
            for j in xrange(i):
                for x in dp[j]:
                    for y in dp[i-j-1]:
                        dp[i].append("("+x+")"+y)
        return dp[n]
