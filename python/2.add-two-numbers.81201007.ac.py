#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers
#
# Medium (27.23%)
# Total Accepted:    292737
# Total Submissions: 1070461
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#         self.val = x
#         self.next = None
def checkNextRound(l1,l2,roundup):
    if roundup == 1:
        return True
    if l1 is not None:
        if l1.next is not None:
           return True
    if l2 is not None:
        if l2.next is not None:
            return True
    return False
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)

        tmp = result
        ptrl1=l1
        ptrl2=l2
        roundup=0
        tmp.val =1
        if ptrl1 is not None:
            a = ptrl1.val
        else:
            a = 0
        if ptrl2 is not None:
            b = ptrl2.val
        else:
            b = 0
        while True:
            tmp.val = (a + b + roundup) 
            if tmp.val > 9:
                roundup = 1
                tmp.val %= 10
            else:
                roundup = 0
            a = 0
            b = 0
            next = False
            if ptrl1 is not None:
                if ptrl1.next is not None:
                    ptrl1 = ptrl1.next
                    a = ptrl1.val
                    next = True
            if ptrl2 is not None:
                if ptrl2.next is not None:
                    ptrl2 = ptrl2.next
                    b = ptrl2.val
                    next = True
            if (next == True) or roundup > 0:
                tmp.next =ListNode(0)
                tmp = tmp.next
            else:
                break
        return result
