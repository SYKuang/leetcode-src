#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (35.96%)
# Total Accepted:    149.6K
# Total Submissions: 415.9K
# Testcase Example:  '[]'
#
#
# Given a binary tree, flatten it to a linked list in-place.
#
#
#
# For example,
# Given
#
# ⁠        1
# ⁠       / \
# ⁠      2   5
# ⁠     / \   \
# ⁠    3   4   6
#
#
#
# The flattened tree should look like:
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠     \
# ⁠      3
# ⁠       \
# ⁠        4
# ⁠         \
# ⁠          5
# ⁠           \
# ⁠            6
#
#
# click to show hints.
#
# Hints:
# If you notice carefully in the flattened tree, each node's right child points
# to the next node of a pre-order traversal.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, root):
        if root is None:
            return None
        tailRight = self.helper(root.right)
        tailLeft = self.helper(root.left)
        if root.left is not None:
            tailLeft.right = root.right
            root.right = root.left
            root.left = None
        if tailRight is not None:
            return tailRight
        elif tailLeft is not None:
            return tailLeft
        else:
            return root
