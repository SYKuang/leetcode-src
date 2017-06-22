#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses
#
# Medium (43.46%)
# Total Accepted:    144088
# Total Submissions: 328481
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
        if n ==0:
            return []
        result=[]
        self.helper(n,n,'',result)
        return result
    def helper(self,left,right,item,Result):
        if right<left:
            return
        if left ==0 and right ==0:
            Result.append(item)
        if left >0:
            self.helper(left-1,right,item+"(",Result)
        if right >0:
            self.helper(left,right-1,item+")",Result)
