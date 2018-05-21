#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (30.88%)
# Total Accepted:    193.5K
# Total Submissions: 626.8K
# Testcase Example:  'No intersection: []\n[]'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
#
# For example, the following two linked lists:
#
# A:          a1 → a2
# ⁠                  ↘
# ⁠                    c1 → c2 → c3
# ⁠                  ↗
# B:     b1 → b2 → b3
#
# begin to intersect at node c1.
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
#
#
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLen(root):
            ret=0
            while root:
                ret+=1
                root=root.next
            return ret
        lenA=getLen(headA)
        lenB=getLen(headB)
        if lenA>lenB:
            for _ in xrange(lenA-lenB):
                headA=headA.next
        elif lenB>lenA:
            for _ in xrange(lenB-lenA):
                headB=headB.next
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None

