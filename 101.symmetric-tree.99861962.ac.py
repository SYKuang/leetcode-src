#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree
#
# Easy (37.96%)
# Total Accepted:    173403
# Total Submissions: 454337
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymetricRec(root.left,root.right)
    def isSymetricRec(self,p,q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        return q.val == p.val and self.isSymetricRec(q.left,p.right) and self.isSymetricRec(q.right,p.left)
        
