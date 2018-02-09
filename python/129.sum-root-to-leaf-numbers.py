#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (37.34%)
# Total Accepted:    127K
# Total Submissions: 339.6K
# Testcase Example:  '[]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
# ⁠   1
# ⁠  / \
# ⁠ 2   3
#
#
#
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
#
# Return the sum = 12 + 13 = 25.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.findNumber(root, 0)
        return self.ret

    def findNumber(self, root, curNum):
        if root is None:
            return
        curNum = curNum * 10 + root.val
        if root.left is None and root.right is None:
            self.ret += curNum
        if root.left:
            self.findNumber(root.left, curNum)
        if root.right:
            self.findNumber(root.right, curNum)
