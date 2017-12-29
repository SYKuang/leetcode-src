#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list
#
# algorithms
# Medium (32.93%)
# Total Accepted:    110.9K
# Total Submissions: 335.5K
# Testcase Example:  '[]\n0'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
#
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small=None
        small_tail=None
        great=None
        great_tail=None
        while head is not None:
            if head.val<x:
                if small_tail==None:
                    small=head
                    small_tail=small
                else:
                    small_tail.next=head
                    small_tail=small_tail.next
            else:
                if great_tail==None:
                   great=head
                   great_tail=great
                else:
                    great_tail.next=head
                    great_tail=great_tail.next
            head=head.next
        if great_tail:
            great_tail.next=None
        if small is not None:
            small_tail.next=great
        else:
            small=great
        return small

