#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image
#
# Medium (38.13%)
# Total Accepted:    112166
# Total Submissions: 294161
# Testcase Example:  '[[1]]'
#
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Follow up:
# Could you do this in-place?
#


class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """
              A             A.transpose         reverse each row
           1  2  3　　　 　　 1  4  7  　　　　　  7  4  1

           4  5  6　　-->　　 2  5  8　　 -->  　  8  5  2　　

           7  8  9 　　　 　　3  6  9　　　　      9  6  3
        """
        for i in xrange(len(matrix)):
            for j in xrange(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = matrix[i][::-1]
