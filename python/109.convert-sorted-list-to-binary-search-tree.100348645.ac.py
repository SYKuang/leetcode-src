#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
#
# Medium (33.38%)
# Total Accepted:    103872
# Total Submissions: 309739
# Testcase Example:  '[]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.refHead=head    
        length=0
        while head is not None:
            length= length+1
            head=head.next
        return self.sortedList2BST(0,length-1)
    def sortedList2BST(self,start,end):
        if start>end:
            return None
        mid=(start+end)/2
        leftTree=self.sortedList2BST(start,mid-1)
        root=TreeNode(self.refHead.val)
        self.refHead=self.refHead.next
        rightTree=self.sortedList2BST(mid+1,end)
        root.left=leftTree
        root.right=rightTree
        return root
        
        
