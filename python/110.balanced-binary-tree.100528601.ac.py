#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree
#
# Easy (36.89%)
# Total Accepted:    171138
# Total Submissions: 461852
# Testcase Example:  '[]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# 
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balaced,_=self.validated(root)
        return balaced
    def validated(self,root):
        if root is None:
            return True,0
        balanced,left=self.validated(root.left)
        if not balanced:
            return False,0
        balanced,right=self.validated(root.right)
        if not balanced:
            return False,0
        return abs(left-right)<=1,max(left,right)+1
