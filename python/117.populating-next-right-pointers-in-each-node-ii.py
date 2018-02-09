#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (33.90%)
# Total Accepted:    117.6K
# Total Submissions: 346.7K
# Testcase Example:  '{}'
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous solution
# still work?
#
# Note:
# You may only use constant extra space.
#
#
# For example,
# Given the following binary tree,
#
# ⁠        1
# ⁠      /  \
# ⁠     2    3
# ⁠    / \    \
# ⁠   4   5    7
#
#
#
# After calling your function, the tree should look like:
#
# ⁠        1 -> NULL
# ⁠      /  \
# ⁠     2 -> 3 -> NULL
# ⁠    / \    \
# ⁠   4-> 5 -> 7 -> NULL
#
#
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        leftMost = root
        while leftMost is not None:
            root = leftMost

            while root and root.right is None and root.left is None:
                root = root.next
            if root is None:
                return
            if root.left:
                leftMost = root.left
            else:
                leftMost = root.right
            cur = leftMost

            while root:
                if cur == root.left:
                    if root.right is not None:
                        cur.next = root.right
                        cur = cur.next
                    root=root.next
                elif cur == root.right:
                    root = root.next
                else: # In this case cur is previors node of root
                    if root.left is None and root.right is None:
                        root = root.next
                    else:
                        if root.left:
                            cur.next = root.left
                        else:
                            cur.next = root.right
                        cur = cur.next
