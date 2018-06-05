#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (34.78%)
# Total Accepted:    19.6K
# Total Submissions: 56.5K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
#
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
#
#
# Example 1:
#
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
#
#
#
#
# Example 2:
#
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
#
#
#
# Note:
#
# The value k is positive and will always be smaller than the length of the
# sorted array.
# ⁠Length of the given array is positive and will not exceed 104
# ⁠Absolute value of elements in the array and x will not exceed 104
#
#
#
#
#
#
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list
# of integers). Please reload the code definition to get the latest changes.
#
#


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = bisect.bisect_left(arr, x)
        if l == 0:
            return arr[:k]
        elif l == len(arr)-1:
            return arr[l-k+1:]
        arr.insert(0, sys.maxint)
        arr.append(sys.maxint)
        start = max(0, l-k)
        end=l
        mid=(start+end)/2
        while start<end:
            if mid+k<len(arr) and abs(arr[mid]-x) >abs(arr[mid+k]-x):
                start=mid+1
            else:
                end=mid
            mid=(start+end)/2
        return arr[mid:mid+k]
