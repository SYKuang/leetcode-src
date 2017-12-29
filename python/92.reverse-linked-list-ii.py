#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii
#
# algorithms
# Medium (30.89%)
# Total Accepted:    123.6K
# Total Submissions: 398.8K
# Testcase Example:  '[5]\n1\n1'
#
#
# Reverse a linked list from position m to n. Do it in-place and in
# one-pass.
#
#
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
#
# return 1->4->3->2->5->NULL.
#
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        count = 0
        while head is not None:
            if count == m - 1:
                break
            head = head.next
            count = count + 1
        Cur = head.next
        ReverseStart = Cur
        Pre = None
        Next = None
        while Cur is not None and count < n:
            Next, Pre, Cur.next = Cur.next, Cur, Pre # Move Next and Pre
            Cur = Next # Next node
            count = count + 1
        ReverseStart.next = Next
        head.next = Pre
        return dummy.next
