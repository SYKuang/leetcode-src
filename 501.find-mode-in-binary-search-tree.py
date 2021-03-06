#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (37.67%)
# Total Accepted:    36.3K
# Total Submissions: 96.2K
# Testcase Example:  '[1,null,2,2]'
#
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the
# most frequently occurred element) in the given BST.
#
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# For example:
# Given BST [1,null,2,2],
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
#
#
#
# return [2].
#
#
# Note:
# If a tree has more than one mode, you can return them in any order.
#
#
# Follow up:
# Could you do that without using any extra space? (Assume that the implicit
# stack space incurred due to recursion does not count).
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p = root
        stack = []
        mx = 0
        cnt = 0
        pre = None
        res = []
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if p.val == pre:
                cnt += 1
            else:
                cnt = 1
            if cnt >= mx:
                if cnt > mx:
                    res = []
                res.append(p.val)
                mx=cnt
            pre = p.val
            p = p.right
        return res
# DFS


class Solution2(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.pre = None
        self.cnt = 0
        self.res = []
        self.mx = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        if self.pre:
            self.cnt = 0 if self.pre.val != root.val else self.cnt+1
        if self.cnt >= self.mx:
            if self.cnt > self.mx:
                self.res = []
            self.res.append(root.val)
            self.mx = self.cnt
        self.pre = root
        self.helper(root.right)
