#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list
#
# Easy (32.19%)
# Total Accepted:    102334
# Total Submissions: 316328
# Testcase Example:  '[]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow=head
        fast=head
        rev=None
        while fast and fast.next:

            fast=fast.next.next
            rev,rev.next,slow=slow,rev,slow.next
        if fast:
            slow=slow.next
        while rev and rev.val == slow.val:
            
            rev=rev.next
            slow=slow.next
        print rev
        return not rev
            
            
            
            
