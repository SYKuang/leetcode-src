#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (46.90%)
# Total Accepted:    37.9K
# Total Submissions: 80.8K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
#
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
#
#
#


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def getDist(i, j):
            return (j[0]-i[0])**2 + (j[1]-i[1])**2
        res = 0
        dp = [collections.defaultdict(int) for _ in xrange(len(points))]
        for i in xrange(len(points)-1):
            for j in xrange(i+1, len(points)):
                dist = getDist(points[i], points[j])
                dp[i][dist] += 1
                dp[j][dist] += 1
        for i in xrange(len(points)):
            for dist in dp[i]:
                n = dp[i][dist]
                if n >= 2:
                    res += n*(n-1)
        return res
