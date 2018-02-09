#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (34.85%)
# Total Accepted:    149.5K
# Total Submissions: 429.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
#
#
# For example:
# Given the below binary tree and sum = 22,
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
#
#
#
# return
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        if root.left == None and root.right == None:
            if root.val != sum:
                return []
            else:
                return [[root.val]]
        Ret = []
        if root.left is not None:
            tmp = self.pathSum(root.left, sum - root.val)
            if len(tmp) > 0:
                for i, v in enumerate(tmp):
                    Ret.append(v)
        if root.right is not None:
            tmp = self.pathSum(root.right, sum - root.val)
            if len(tmp) > 0:
                for i, v in enumerate(tmp):
                    Ret.append(v)
        for i, v in enumerate(Ret):
            Ret[i] = [root.val] + v
        return Ret
