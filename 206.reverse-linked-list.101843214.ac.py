#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list
#
# Easy (44.67%)
# Total Accepted:    223802
# Total Submissions: 498698
# Testcase Example:  '[]'
#
# Reverse a singly linked list.
# 
# click to show more hints.
# 
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, curr, preceding = None, head, head.next
        while preceding:
            curr.next = pre
            pre = curr
            curr = preceding
            preceding = preceding.next
        curr.next = pre
        return curr

