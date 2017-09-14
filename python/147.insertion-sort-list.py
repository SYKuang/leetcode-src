#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list
#
# Medium (32.76%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '[]'
#
# Sort a linked list using insertion sort.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        while head:
            p = dummyHead
            while p.next and p.next.val < head.val:
                p = p.next
            tmp = head.next
            head.next = p.next
            p.next = head
            head = tmp
        return dummyHead.next
