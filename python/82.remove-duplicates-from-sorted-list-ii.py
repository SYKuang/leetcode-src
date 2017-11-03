#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
#
# algorithms
# Medium (29.60%)
# Total Accepted:    120.2K
# Total Submissions: 405.4K
# Testcase Example:  '[]'
#
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.ret = ListNode(0)
        self.retCur = self.ret
        skip = False
        pre = None
        while head:
            if skip:
                if pre != head.val:
                    skip = False
                    pre = None
                    continue
            elif not head.next:
                self.addNode(head)
            elif head.val != head.next.val:
                self.addNode(head)
            else:
                skip = True
                pre = head.val
            head = head.next
        self.retCur.next = None
        return self.ret.next

    def addNode(self, node):
        self.retCur.next = node
        self.retCur = self.retCur.next
