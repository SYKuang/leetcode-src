#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
#
# algorithms
# Medium (35.16%)
# Total Accepted:    118.4K
# Total Submissions: 332.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [20,9],
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

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        fromR = False
        ret = []
        levelQ = []
        count = 0
        if root:
            levelQ.append(root)
            count = count + 1
            fromR = True
        while count != 0:
            size = count
            count = 0
            tmp = []
            tmpQ = levelQ[:size]
            levelQ = levelQ[size:]
            for i in xrange(size):
                tmp.append(tmpQ[i].val)
                if fromR:
                    if tmpQ[i].left:
                        levelQ.insert(0, tmpQ[i].left)
                        count = count + 1
                    if tmpQ[i].right:
                        levelQ.insert(0, tmpQ[i].right)
                        count = count + 1
                else:
                    if tmpQ[i].right:
                        levelQ.insert(0, tmpQ[i].right)
                        count = count + 1
                    if tmpQ[i].left:
                        levelQ.insert(0, tmpQ[i].left)
                        count = count + 1
            if fromR:
                fromR = False
            else:
                fromR = True
            ret.append(tmp)
        return ret
