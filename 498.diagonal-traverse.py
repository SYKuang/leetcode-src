#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (45.53%)
# Total Accepted:    21K
# Total Submissions: 46.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
#
#
# Example:
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:
#
#
#
#
# Note:
#
# The total number of elements of the given matrix will not exceed 10,000.
#
#
#


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        directs = ((-1, 1), (1, -1))
        d = 0
        q = collections.deque()
        q.append((0, 0))
        res = []
        while len(res) < m*n:
            x, y = q.popleft()
            res.append(matrix[x][y])
            nx, ny = x+directs[d][0], y+directs[d][1]
            if not(0 <= nx < m and 0 <= ny < n):
                if nx >= m:
                    nx = m-1
                    ny += 2
                    d = (d+1) % 2
                if ny >= n:
                    ny = n-1
                    nx += 2
                    d = (d+1) % 2
                if ny == -1:
                    ny = 0
                    d = (d+1) % 2
                if nx == -1:
                    nx = 0
                    d = (d+1) % 2
            q.append((nx, ny))
        return res
