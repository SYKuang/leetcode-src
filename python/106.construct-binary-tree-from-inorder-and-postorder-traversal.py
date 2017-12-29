#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
#
# algorithms
# Medium (32.40%)
# Total Accepted:    96.1K
# Total Submissions: 294.8K
# Testcase Example:  '[]\n[]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 1:
            return TreeNode(inorder[-1])
        elif len(inorder) == 0:
            return None

        node = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])

        leftPost = postorder[:index]
        leftIn = inorder[:index]
        rightPost = postorder[index:-1]
        rightIn = inorder[index + 1:]
        if len(leftPost) > 0:
            node.left = self.buildTree(leftIn, leftPost)
        if len(rightPost) > 0:
            node.right = self.buildTree(rightIn, rightPost)
        return node
