#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (37.00%)
# Total Accepted:    14K
# Total Submissions: 37.9K
# Testcase Example:  '[2,1,1]'
#
#
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them.
#
#
# Two trees are duplicate if they have the same structure with same node
# values.
#
#
# Example 1:
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
#
# The following are two duplicate subtrees:
#
# ⁠     2
# ⁠    /
# ⁠   4
#
# and
#
# ⁠   4
#
# Therefore, you need to return above trees' root in the form of a list.
#
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
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.ret = []
        self.table = collections.defaultdict(int)
        self.helper(root)
        return self.ret

    def helper(self, root):
        if not root:
            return "#"
        s = str(root.val)+","+self.helper(root.left) + \
            ","+self.helper(root.right)
        if self.table[s] == 1:
            self.ret.append(root)
        self.table[s] += 1
        return s
