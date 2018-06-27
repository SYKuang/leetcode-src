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
        if n == 0:
            return [""]
        pre = self.generateParenthesis(n-1)
        res = set()
        for p in pre:
            for i, c in enumerate(p):
                if c == "(":
                    res.add(p[:i+1]+"()"+p[i+1:])
            res.add("()"+p)
        return list(res)
