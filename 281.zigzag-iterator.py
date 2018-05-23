#
# [281] Zigzag Iterator
#
# https://leetcode.com/problems/zigzag-iterator/description/
#
# algorithms
# Medium (52.89%)
# Total Accepted:    38K
# Total Submissions: 71.9K
# Testcase Example:  '[1,2]\n[3,4,5,6]'
#
# Given two 1d vectors, implement an iterator to return their elements
# alternately.
#
# Example:
#
#
# Input:
# v1 = [1,2]
# v2 = [3,4,5,6]
#
# Output: [1,3,2,4,5,6]
#
# Explanation: By calling next repeatedly until hasNext returns
# false,
# the order of elements returned by next should be: [1,3,2,4,5,6].
#
# Follow up: What if you are given k 1d vectors? How well can your code be
# extended to such cases?
#
# Clarification for the follow up question:
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
# If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For
# example:
#
#
# Input:
# [1,2,3]
# [4,5,6,7]
# [8,9]
#
# Output: [1,4,8,2,5,9,3,6,7].
#
#
#


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.stack = collections.deque()
        for a, b in zip(v1, v2):
            self.stack.append(a)
            self.stack.append(b)

        if len(v2) > len(v1):
            for n in v2[len(v1):]:
                self.stack.append(n)
        elif len(v1) > len(v2):
            for n in v1[len(v2):]:
                self.stack.append(n)

    def next(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.popleft()
        return -1

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
