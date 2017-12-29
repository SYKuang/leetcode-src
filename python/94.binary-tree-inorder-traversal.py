#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal
#
# algorithms
# Medium (47.33%)
# Total Accepted:    233.9K
# Total Submissions: 489.6K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
#
# For example:
# Given binary tree [1,null,2,3],
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
#
#
# return [1,3,2].
#
#
# Note: Recursive solution is trivial, could you do it iteratively?
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        stack = []
        ret = []
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack[-1]
                stack.pop()
                ret.append(cur.val)
                cur = cur.right
        return ret
