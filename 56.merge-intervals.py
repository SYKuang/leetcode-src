#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (32.16%)
# Total Accepted:    201.2K
# Total Submissions: 625.5K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
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
        res = []

        def compare(a, b):
            if a.start != b.start:
                return a.start-b.start
            else:
                return b.end-a.end
        intervals.sort(cmp=compare)
        for inter in intervals:
            if res and res[-1].end >= inter.start:
                res[-1].end = max(res[-1].end, inter.end)
            else:
                res.append(inter)
        return res
