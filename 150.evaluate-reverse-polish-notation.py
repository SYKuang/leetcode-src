#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (28.66%)
# Total Accepted:    116.8K
# Total Submissions: 407.2K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
#
# Note:
#
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
#
#
# Example 1:
#
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
#
# Example 2:
#
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
#
# Example 3:
#
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def cals(a, b, oper):
            if oper == "+":
                return a+b
            elif oper == "-":
                return a-b
            elif oper == "*":
                return a*b
            else:
                return int(float(a)/b)
        stack = []
        for c in tokens:
            if c in ("+", "-", "*", "/"):
                b, a = stack.pop(), stack.pop()
                r = cals(a, b, c)
                stack.append(r)
            else:
                stack.append(int(c))
        return stack[-1]
