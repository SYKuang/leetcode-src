#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#
# Easy (41.40%)
# Total Accepted:    122583
# Total Submissions: 294591
# Testcase Example:  '[]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createTree(nums)
    def createTree(self,nums):
        if len(nums) == 0:
            return None
        elif len(nums)==1:
            newNode=TreeNode(nums[0])
            
            return newNode
        elif len(nums)==2:
            newNode=TreeNode(nums[0])
            RightNode=TreeNode(nums[1])
            newNode.right=RightNode
            return newNode
        newNode = TreeNode(nums[len(nums)/2])
        newNode.left=self.createTree(nums[0:len(nums)/2])
        newNode.right=self.createTree(nums[len(nums)/2+1:])
        return newNode
        
