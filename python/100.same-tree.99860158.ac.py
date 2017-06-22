#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree
#
# Easy (45.92%)
# Total Accepted:    200482
# Total Submissions: 434944
# Testcase Example:  '[]\n[]'
#
# 
# Given two binary trees, write a function to check if they are equal or not.
# 
# 
# Two binary trees are considered equal if they are structurally identical and
# the nodes have the same value.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is  None or q is  None:
            return False
        #print str(p.val == q.val)
        #print str(self.isSameTree(q.left,p.left))
        #print str(self.isSameTree(q.right,p.right))
        return p.val == q.val and self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)
