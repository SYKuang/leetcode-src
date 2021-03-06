#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (40.15%)
# Total Accepted:    58.3K
# Total Submissions: 145.3K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
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
        :rtype: int
        """
        self.ret = 0
        pathTable = collections.defaultdict(int)
        pathTable[0] = 1

        def helper(root, pathSum, target):
            if not root:
                return
            pathSum += root.val
            if pathTable[(pathSum - target)] != 0:
                self.ret += pathTable[(pathSum - target)]
            pathTable[pathSum] += 1
            helper(root.left, pathSum, target)
            helper(root.right, pathSum, target)
            pathTable[pathSum] -= 1
        helper(root, 0, sum)
        return self.ret


""" Beats 50%
        self.ret = 0
        self.helper(root, sum, [])
        return self.ret

    def helper(self, root, sum, parents):
        if not root:
            return
        if root.val == sum:
            self.ret += 1
        for i in xrange(len(parents)):
            parents[i] += root.val
            if parents[i] == sum:
                self.ret += 1
        parents.append(root.val)
        self.helper(root.left, sum, parents)
        self.helper(root.right, sum, parents)
        parents.pop()
        for i in xrange(len(parents)):
            parents[i] -= root.val
        return
"""
