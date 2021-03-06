#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (29.61%)
# Total Accepted:    11.4K
# Total Submissions: 38.6K
# Testcase Example:  '"()"'
#
#
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#
#
#


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stackL = []
        stackS = []
        for i, c in enumerate(s):
            if c == "(":
                stackL.append(i)
            elif c == "*":
                stackS.append(i)
            else:
                if stackL:
                    stackL.pop()
                else:
                    if stackS:
                        stackS.pop()
                    else:
                        return False
        if len(stackL) > len(stackS):
            return False
        while stackL:
            if stackL[-1] > stackS[-1]:
                return False
            stackL.pop()
            stackS.pop()
        return True
