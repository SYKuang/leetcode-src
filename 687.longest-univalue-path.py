#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (32.80%)
# Total Accepted:    25.6K
# Total Submissions: 77.9K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of
# edges between them.
#
#
# Example 1:
#
#
#
#
# Input:
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
#
#
# Output:
#
# 2
#
#
#
#
# Example 2:
#
#
#
#
# Input:
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
#
#
# Output:
#
# 2
#
#
#
# Note:
# The given binary tree has not more than 10000 nodes.  The height of the tree
# is not more than 1000.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        ret = self.helper(root)
        self.ret = max(self.ret, ret)
        return self.ret

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if root.right and root.val == root.right.val:
            right += 1
        else:
            right = 0
        if root.left and root.val == root.left.val:
            left += 1
        else:
            left = 0
        self.ret = max(self.ret, right+left)
        return max(right, left)
