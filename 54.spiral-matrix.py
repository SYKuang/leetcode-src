#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (27.52%)
# Total Accepted:    147K
# Total Submissions: 534.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        res = []
        x, y = (0, 0)
        visited = set()
        while len(res) < m*n:
            res.append(matrix[x][y])
            visited.add((x, y))
            nx = directs[0][0]+x
            ny = directs[0][1]+y
            if nx >= m or nx < 0 or ny >= n or ny < 0 or (nx, ny) in visited:
                directs.append(directs[0])
                directs.pop(0)
                nx = directs[0][0]+x
                ny = directs[0][1]+y
            x = nx
            y = ny
        return res
