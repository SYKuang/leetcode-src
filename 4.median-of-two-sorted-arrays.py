#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (23.27%)
# Total Accepted:    263.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
#
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#
#


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1)+len(nums2)) % 2:
            return self.helper(nums1, nums2, (len(nums1)+len(nums2))/2+1)*1.0
        else:
            return (self.helper(nums1, nums2, (len(nums1)+len(nums2))/2)*1. +
                    self.helper(nums1, nums2, (len(nums1)+len(nums2))/2+1)*1.)/2

    def helper(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.helper(nums2, nums1, k)
        if not nums1:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        if (len(nums1)+len(nums2)) == k:
            return max(nums1[-1], nums2[-1])
        idx1 = min(k//2, len(nums1))
        idx2 = k-idx1
        if nums1[idx1-1] > nums2[idx2-1]:
            return self.helper(nums1, nums2[idx2:], k-idx2)
        else:
            return self.helper(nums1[idx1:], nums2, k-idx1)
