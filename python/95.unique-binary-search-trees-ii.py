#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii
#
# algorithms
# Medium (31.65%)
# Total Accepted:    91.6K
# Total Submissions: 288.7K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1...n.
#
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        ret = []
        if start > end:
            return [None]
        for i in xrange(start, end + 1):
            left = self.helper(start, i - 1)
            right = self.helper(i + 1, end)
            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    ret.append(node)
        return ret
