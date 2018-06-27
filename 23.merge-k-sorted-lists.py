#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (28.94%)
# Total Accepted:    237.8K
# Total Submissions: 820.3K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
#
# Example:
#
#
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        arr = []
        nodes = []
        for ll in lists:
            while ll:
                arr.append(ll.val)
                nodes.append(ll)
                ll = ll.next
        arr.sort()
        for i in xrange(len(arr)):
            nodes[i].val = arr[i]
            if i+1 < len(arr):
                nodes[i].next = nodes[i+1]
            else:
                nodes[i].next = None
        if len(arr):
            return nodes[0]
        else:
            return None
