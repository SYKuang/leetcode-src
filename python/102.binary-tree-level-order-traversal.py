#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal
#
# algorithms
# Medium (40.48%)
# Total Accepted:    203K
# Total Submissions: 494.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        count = 0
        ret = []
        levelQ = []
        if root is not None:
            count = count + 1
            levelQ.append(root)
        while count != 0:
            size = count
            count = 0
            tmp = []
            for i in xrange(size):
                tmp.append(levelQ[i].val)
                if levelQ[i].left is not None:
                    levelQ.append(levelQ[i].left)
                    count = count + 1
                if levelQ[i].right is not None:
                    levelQ.append(levelQ[i].right)
                    count = count + 1
            levelQ = levelQ[size:]
            ret.append(tmp)
        return ret
