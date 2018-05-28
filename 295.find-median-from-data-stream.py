#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (30.02%)
# Total Accepted:    62K
# Total Submissions: 206.4K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
#
# [2,3,4] , the median is 3 
#
# [2,3], the median is (2 + 3) / 2 = 2.5 
#
# Design a data structure that supports the following two operations:
#
#
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
#
#
# Example:
#
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
#
#


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.right = []
        self.left = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.left, -num)
        heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) > len(self.right) :
            return -self.left[0]*1.
        else:
            return (-self.left[0]+self.right[0])/2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
