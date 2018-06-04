#
# [356] Line Reflection
#
# https://leetcode.com/problems/line-reflection/description/
#
# algorithms
# Medium (30.31%)
# Total Accepted:    14.4K
# Total Submissions: 47.6K
# Testcase Example:  '[[1,1],[-1,1]]'
#
# Given n points on a 2D plane, find if there is such a line parallel to y-axis
# that reflect the given points.
#
#
# ⁠   Example 1:
#
#
# Given points = [[1,1],[-1,1]], return true.
#
#
#
# ⁠   Example 2:
#
#
# Given points = [[1,1],[-1,-1]], return false.
#
#
# Follow up:
# Could you do better than O(n2)?
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        points = set([(x, y) for x, y in points])
        xs = [x for x,_ in points]
        xs.sort()
        l = len(xs)
        if l < 2:
            return True
        line = xs[l//2] if l % 2 else 1.0*(xs[l//2]+xs[l//2-1])/2
        for x, y in points:
            if (2*line-x, y) not in points:
                return False
        return True
