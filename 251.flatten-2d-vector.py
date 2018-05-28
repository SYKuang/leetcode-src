#
# [251] Flatten 2D Vector
#
# https://leetcode.com/problems/flatten-2d-vector/description/
#
# algorithms
# Medium (41.58%)
# Total Accepted:    37.5K
# Total Submissions: 90.3K
# Testcase Example:  '[[1,2],[3],[4,5,6]]'
#
# Implement an iterator to flatten a 2d vector.
#
# Example:
#
#
# Input: 2d vector =
# [
# ⁠ [1,2],
# ⁠ [3],
# ⁠ [4,5,6]
# ]
# Output: [1,2,3,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns
# false,
# the order of elements returned by next should be: [1,2,3,4,5,6].
#
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or
# iterators in Java.
#
#


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.row = 0
        self.index = 0

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.vec2d[self.row][self.index-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec2d) and self.index >= len(self.vec2d[self.row]):
            self.row += 1
            self.index = 0
        return self.row != len(self.vec2d)
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
