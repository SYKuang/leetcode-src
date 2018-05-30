#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (39.61%)
# Total Accepted:    70.6K
# Total Submissions: 178.1K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
#
# Example 1:
#
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
#
# Example 2:
#
#
# Input: [[7,10],[2,4]]
# Output: 1
#
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda inter: inter.start)
        rooms = []
        for inter in intervals:
            new = True
            for i, r in enumerate(rooms):
                if r.end <= inter.start:
                    rooms[i] = inter
                    new = False
                    break
            if new:
                rooms.append(inter)
        return len(rooms)
