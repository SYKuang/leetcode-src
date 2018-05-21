#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (39.76%)
# Total Accepted:    61.3K
# Total Submissions: 154.2K
# Testcase Example:  '[1,2,3,4,5]'
#
#
# Given an unsorted array return whether an increasing subsequence of length 3
# exists or not in the array.
#
#
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1
# else return false.
#
#
#
# Your algorithm should run in O(n) time complexity and O(1) space
# complexity.
#
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
#
# Given [5, 4, 3, 2, 1],
# return false.
#
#
# Credits:Special thanks to @DjangoUnchained for adding this problem and
# creating all test cases.
#


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m1 = sys.maxint
        m2 = sys.maxint
        for n in nums:
            if m1 >= n:  # m1 always remember smallest number
                m1 = n
            elif m2 >= n:  # We can found a number > m1
                m2 = n
            else:  # There exist a number larger than m1 and m2
                return True
        return False
