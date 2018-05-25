#
# [685] Redundant Connection II
#
# https://leetcode.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (27.68%)
# Total Accepted:    7K
# Total Submissions: 25.3K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
#
# In this problem, a rooted tree is a directed graph such that, there is
# exactly one node (the root) for which all other nodes are descendants of this
# node, plus every node has exactly one parent, except for the root node which
# has no parents.
#
# The given input is a directed graph that started as a rooted tree with N
# nodes (with distinct values 1, 2, ..., N), with one additional directed edge
# added.  The added edge has two different vertices chosen from 1 to N, and was
# not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] that represents a directed edge connecting nodes u and v,
# where u is a parent of child v.
#
# Return an edge that can be removed so that the resulting graph is a rooted
# tree of N nodes.  If there are multiple answers, return the answer that
# occurs last in the given 2D-array.
# Example 1:
#
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
#
#
# Example 2:
#
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5  2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4
#
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
#
#


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [0]*(len(edges)+1)

        def find(root):
            while root != parent[root]:
                root = parent[root]
            return root
        first = []
        second = []
        for i, (u, v) in enumerate(edges):
            if parent[v] == 0:
                parent[v] = u
            else:
                # Exist a point which has indegree equals 2
                first = [parent[v], v]
                second = [u, v]
                edges[i][1] = 0  # Break edge
        for i in xrange(1, len(edges)+1):
            parent[i] = i
        for u, v in edges:
            if v == 0:
                continue
            p1 = find(u)
            p2 = find(v)
            # Exist Cycle
            if p1 == p2:
                if first:  # Exist cycle and a point has indegree equals 2
                    return first
                else:  # Exist cycle but not point has indegree equals 2
                    return [u, v]
            parent[p2] = p1
        # After remove edge, there is no cycle. return the edge which will make
        # indegre equals 2
        return second
