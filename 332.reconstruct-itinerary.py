#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (30.05%)
# Total Accepted:    50.6K
# Total Submissions: 168.3K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
#
# Note:
#
#
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
#
#
# Example 1:
#
#
# Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR",
# "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
#
#
# Example 2:
#
#
# Input: tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
#
#
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test
# cases.
#
#


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort(key=lambda x: x[0]+x[1])
        table = collections.defaultdict(list)
        for f, t in tickets:
            table[f].append(t)
        q = ["JFK"]
        res = []
        while q:
            start = q[-1]
            if not table[start]:
                res.insert(0, start)
                q.pop()
            else:
                q.append(table[start][0])
                table[start].pop(0)
        return res


class Solution2(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.table = collections.defaultdict(list)
        tickets.sort(key=lambda x: x[0]+x[1])
        for f, t in tickets:
            self.table[f].append(t)
        self.res = []
        self.dfs("JFK")
        return self.res[::-1]

    def dfs(self, start):
        while self.table[start]:
            nextStart = self.table[start][0]
            self.table[start].pop(0)
            self.dfs(nextStart)
        self.res.append(start)
