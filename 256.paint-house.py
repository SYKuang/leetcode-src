#
# [256] Paint House
#
# https://leetcode.com/problems/paint-house/description/
#
# algorithms
# Easy (46.13%)
# Total Accepted:    35.7K
# Total Submissions: 77.4K
# Testcase Example:  '[[17,2,17],[16,16,5],[14,3,19]]'
#
# There are a row of n houses, each house can be painted with one of the three
# colors: red, blue or green. The cost of painting each house with a certain
# color is different. You have to paint all the houses such that no two
# adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x
# 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color red; costs[1][2] is the cost of painting house 1 with color green, and
# so on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Example:
#
#
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2
# into blue.
# Minimum cost: 2 + 5 + 3 = 10.
#
#
#


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        min1 = 0
        min2 = 0
        idx1 = -1
        for cost in costs:
            m1 = sys.maxint
            m2 = m1
            id1 = -1
            for i, c in enumerate(cost):
                c += min2 if i == idx1 else min1
                if c < m1:
                    m2 = m1
                    m1 = c
                    id1 = i
                elif c < m2:
                    m2 = c
            min1, min2, idx1 = m1, m2, id1
        return min1
