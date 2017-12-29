#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree
#
# algorithms
# Medium (23.55%)
# Total Accepted:    198.1K
# Total Submissions: 834.5K
# Testcase Example:  '[2,1,3]'
#
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
#
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Binary tree [2,1,3], return true.
#
#
# Example 2:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   3
#
# Binary tree [1,2,3], return false.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left:
            if not self.isValidBSTLR(root.left, -sys.maxint - 1, root.val):
                return False
        if root.right:
            if not self.isValidBSTLR(root.right, root.val, sys.maxint):
                return False
        return True

    def isValidBSTLR(self, root, Min, Max):
        if root.val >= Max or root.val <= Min:
            return False
        if root.left:
            if not self.isValidBSTLR(root.left, Min, root.val):
                return False

        if root.right:
            if not self.isValidBSTLR(root.right, root.val, Max):
                return False
        return True
