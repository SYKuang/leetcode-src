#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
#
# algorithms
# Medium (32.60%)
# Total Accepted:    119.3K
# Total Submissions: 363.5K
# Testcase Example:  '[]\n[]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
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

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        if len(inorder)  == 1:
            return node
        index = inorder.index(preorder[0])
        leftPre=preorder[1:index+1]
        leftIn=inorder[:index]
        rightPre=preorder[index+1:]
        rightIn=inorder[index+1:]
        if len(leftPre) >0:
            node.left = self.buildTree(leftPre, leftIn)
        if len(rightPre)>0:
            node.right = self.buildTree(rightPre, rightIn)
        return node
