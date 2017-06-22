#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals
#
# Medium (29.49%)
# Total Accepted:    125242
# Total Submissions: 424045
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
#
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        # self.sort(intervals)
        intervals = sorted(intervals, key=lambda x: x.start)

        rets = []
        rets.append(intervals[0])
        for interval in intervals:
            if rets[-1].end >= interval.start:
                rets[-1].end = max(interval.end, rets[-1].end)
            else:
                rets.append(interval)
        return rets

    def sort(self, intervals):
        for i in xrange(len(intervals)):
            for j in xrange(0, len(intervals) - 1 - i):
                if intervals[j].start > intervals[j + 1].start:
                    intervals[j], intervals[
                        j + 1] = intervals[j + 1], intervals[j]
