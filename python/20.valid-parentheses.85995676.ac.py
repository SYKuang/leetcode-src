#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses
#
# Easy (32.95%)
# Total Accepted:    200154
# Total Submissions: 604739
# Testcase Example:  '"["'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for c in s:
            if self.isLeft(c):
                stack.append(c)
            else:
                if len(stack) ==0:
                    return False
                if stack.pop() != self.getLeft(c):
                    
        
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
    def isLeft(self,x):
        return {
            '(': True,
            '{': True,
            '[': True,
        }.get(x,False)
    
    def getLeft(self,x):
        return {
            ')': '(',
            ']': '[',
            '}': '{',
        }.get(x,x)
