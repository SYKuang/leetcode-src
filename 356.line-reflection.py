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
        if len(points)<=1:
            return True
        sPoints = set()
        for a, b in points:
            sPoints.add((a, b))
        sPoints = list(sPoints)
        sPoints.sort(key=lambda x: x[0])
        line = sPoints[len(sPoints)//2][0] if len(sPoints) % 2 else 1.0*(
            sPoints[len(sPoints)//2][0]+sPoints[(len(sPoints)//2)-1][0])/2
        for x, y in sPoints:
            if (2*line-x, y) not in sPoints:
                return False
        return True
