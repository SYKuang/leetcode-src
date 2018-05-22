#
# [265] Paint House II
#
# https://leetcode.com/problems/paint-house-ii/description/
#
# algorithms
# Hard (38.48%)
# Total Accepted:    31.4K
# Total Submissions: 81.6K
# Testcase Example:  '[[1,5,3],[2,9,4]]'
#
# There are a row of n houses, each house can be painted with one of the k
# colors. The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the
# same color.
#
# The cost of painting each house with a certain color is represented by a n x
# k cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color 0; costs[1][2] is the cost of painting house 1 with color 2, and so
# on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Example:
#
#
# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum
# cost: 1 + 4 = 5;
# Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 +
# 2 = 5.
#
#
# Follow up:
# Could you solve it in O(nk) runtime?
#
#


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        min1 = 0
        min2 = 0
        idx1 = -1
        for i, row in enumerate(costs):
            m1 = sys.maxint
            m2 = m1
            id1 = -1
            for j, cost in enumerate(row):
                cost += min1 if j != idx1 else min2
                if cost < m1:
                    m2 = m1
                    m1 = cost
                    id1 = j
                elif cost < m2:
                    m2 = cost
            idx1 = id1
            min1 = m1
            min2 = m2
        return min1
