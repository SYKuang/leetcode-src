#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list
#
# algorithms
# Medium (24.34%)
# Total Accepted:    119.2K
# Total Submissions: 489.8K
# Testcase Example:  '[]\n0'
#
# Given a list, rotate the list to the right by k places, where k is
# non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        tail = head
        length = 1
        while tail.next != None:
            length = length + 1
            tail = tail.next
        if (k % length) == 0:
            return head
        tail.next = head
        length = length - (k % length)
        tail = head
        for i in xrange(length, 1, -1):
            tail = tail.next
        newHead = tail.next
        tail.next = None
        return newHead
