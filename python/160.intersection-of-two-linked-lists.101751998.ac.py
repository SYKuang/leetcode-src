#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists
#
# Easy (30.32%)
# Total Accepted:    128793
# Total Submissions: 423606
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
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            if headA == headB:
                return headA
        else:
            return None

        oriHeadA, oriHeadB = headA, headB
        LastA, LastB = None, None

        while headA and headB:
            if headA.next is None:
                LastA = headA
                if LastB:
                    if LastA != LastB:
                        return None
                headA = oriHeadB
            else:
                headA = headA.next
                if headA == oriHeadB:
                    return headA

            if headB.next is None:
                LastB = headB
                headB = oriHeadA
                if LastA:
                    if LastA != LastB:
                        return None
            else:
                headB = headB.next
                if headB == oriHeadA:
                    return headB

            if headA == headB or headA.val == headB.val:
                return headA

