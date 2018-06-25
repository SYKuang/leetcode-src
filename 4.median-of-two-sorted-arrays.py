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
        if (len(nums2)+len(nums1)) % 2:
            return 1.0*self.findKth(nums1, nums2, (len(nums2)+len(nums1))//2+1)
        else:
            return 1.0*(self.findKth(nums1, nums2, (len(nums2)+len(nums1))//2+1)+self.findKth(nums1, nums2, (len(nums2)+len(nums1))//2))/2

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKth(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        p1 = min(len(nums1), k//2)
        p2 = k-p1
        if nums1[p1-1] > nums2[p2-1]:
            return self.findKth(nums1, nums2[p2:], k-p2)
        else:
            return self.findKth(nums1[p1:], nums2, k-p1)
