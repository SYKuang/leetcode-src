#
# [373] Find K Pairs with Smallest Sums
#
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (31.41%)
# Total Accepted:    42.2K
# Total Submissions: 134.3K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
#
# You are given two integer arrays nums1 and nums2 sorted in ascending order
# and an integer k.
#
#
# Define a pair (u,v) which consists of one element from the first array and
# one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
#
#
# Example 1:
#
# Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
#
# Return: [1,2],[1,4],[1,6]
#
# The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
#
#
# Example 2:
#
# Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2
#
# Return: [1,1],[1,1]
#
# The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
#
#
# Example 3:
#
# Given nums1 = [1,2], nums2 = [3],  k = 3
#
# Return: [1,3],[2,3]
#
# All possible pairs are returned from the sequence:
# [1,3],[2,3]
#
#
#
# Credits:Special thanks to @elmirap and @StefanPochmann for adding this
# problem and creating all test cases.
#


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        res = []
        q = []
        heapq.heappush(q, (nums1[0]+nums2[0], 0, 0))
        while len(res) < k and q:
            _, i, j = heapq.heappop(q)
            if j == 0 and i < len(nums1)-1:
                heapq.heappush(q, (nums1[i+1]+nums2[j], i+1, j))
            if j < len(nums2)-1:
                heapq.heappush(q, (nums1[i]+nums2[j+1], i, j+1))
            res.append([nums1[i], nums2[j]])
        return res
