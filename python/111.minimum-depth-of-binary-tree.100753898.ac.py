#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree
#
# Easy (32.75%)
# Total Accepted:    164328
# Total Submissions: 500293
# Testcase Example:  '[]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif (root.right is None and root.left is not None):
            return self.minDepth(root.left)+1
        elif (root.left is None and root.right is not None):
            return self.minDepth(root.right)+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1

