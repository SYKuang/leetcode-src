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
        ret = max(self.helper(root))
        return ret

    def helper(self, root):
        if not root:
            return [0, 0]
        robLeft = self.helper(root.left)
        robRight = self.helper(root.right)
        nRob = robLeft[0]+robRight[0]
        Rob = robLeft[1]+robRight[1]+root.val
        return [max(nRob, Rob), nRob]
