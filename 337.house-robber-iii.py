#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (44.88%)
# Total Accepted:    66.3K
# Total Submissions: 147.8K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same
# night.
#
#
#
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
#
#
# Example 1:
#
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \
# ⁠    3   1
#
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
#
# Example 2:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \
# ⁠1   3   1
#
# Maximum amount of money the thief can rob = 4 + 5 = 9.
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mem = {}
        ret = max(self.helper(root, False), self.helper(root, True))
        return ret

    def helper(self, root, rob):
        if not root:
            return 0
        if (root, rob) in self.mem:
            return self.mem[(root, rob)]
        if not root.left and not root.right:
            if rob:
                return 0
            else:
                return root.val
        if rob:
            ret = self.helper(root.left, False)+self.helper(root.right, False)
        else:
            retRob = self.helper(root.left, True)+self.helper(root.right, True)
            retNRob = self.helper(root.left, False) + \
                self.helper(root.right, False)
            ret = max(root.val+retRob, retNRob)
        self.mem[(root, rob)] = ret
        return ret
