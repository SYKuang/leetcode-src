#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists
#
# Easy (38.62%)
# Total Accepted:    220923
# Total Submissions: 569818
# Testcase Example:  '[]\n[]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptrL1=l1
        ptrL2=l2
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            res=l2
            ptrL2=l2.next
        else:
            res=l1
            ptrL1=l1.next
        tmp=res
        while (ptrL1 is not None) or (ptrL2 is not None):
            if ptrL1 is None:
                tmp.next=ptrL2
                return res
            elif ptrL2 is None:
                tmp.next=ptrL1
                return res
            else:
                if ptrL1.val > ptrL2.val:
                    tmp.next=ListNode(ptrL2.val)
                    ptrL2=ptrL2.next
                    tmp=tmp.next
                else:
                    tmp.next=ListNode(ptrL1.val)
                    ptrL1=ptrL1.next
                    tmp=tmp.next
        return res
                
        
