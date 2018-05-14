#
# [346] Moving Average from Data Stream
#
# https://leetcode.com/problems/moving-average-from-data-stream/description/
#
# algorithms
# Easy (60.53%)
# Total Accepted:    40K
# Total Submissions: 66K
# Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
#
# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.
#
# For example,
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
#
#
#


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.count = 0
        self.size = size
        self.data = []
        self.ans = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.count < self.size:
            self.ans *= self.count
            self.data.append(val)
        else:
            self.ans *= self.size
            self.ans -= self.data[self.count % self.size]
            self.data[self.count % self.size] = val
        self.count += 1
        self.ans += val
        self.ans /= float(len(self.data))
        return self.ans


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
