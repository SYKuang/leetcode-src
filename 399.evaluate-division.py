#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (42.53%)
# Total Accepted:    30.5K
# Total Submissions: 71.7K
# Testcase Example:  '[ ["a","b"],["b","c"] ]\n[2.0,3.0]\n[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]'
#
#
# Equations are given in the format A / B = k, where  A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given  a / b = 2.0, b / c = 3.0. queries are:  a / c = ?,  b / a = ?, a / e =
# ?,  a / a = ?, x / x = ? . return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
#
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
#
#
# According to the example above:
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
#
#
#
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
#
#


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.connect = collections.defaultdict(list)
        for (a, b), v in zip(equations, values):
            self.connect[a].append((b, v))
            self.connect[b].append((a, 1/v))

        def findValue(a, b,visited):


            if a not in self.connect or b not in self.connect:
                return -1.0
            if a == b:
                return 1.0
            if a in visited:
                return -1
            visited.add(a)
            for t in self.connect[a]:
                if t[0] == b:
                    return t[1]
                tmp = findValue(t[0], b,visited)
                if tmp != -1:
                   return t[1]*tmp
            return -1
        ret = []
        for (a, b) in queries:
            ret.append(findValue(a, b,set()))
        return ret
