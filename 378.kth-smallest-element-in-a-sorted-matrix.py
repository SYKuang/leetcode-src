#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (45.62%)
# Total Accepted:    63K
# Total Submissions: 138K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
#
#
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
#
#
# Example:
#
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.
#


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        while lo < hi:
            mid = (lo+hi)//2
            lower = self.count(matrix, mid)
            if lower < k:
                lo = mid+1
            else:
                hi = mid
        return hi

    def count(self, matrix, num):
        i = len(matrix)-1
        j = 0
        count = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= num:
                count += i+1
                j += 1
            else:
                i -= 1
        return count
