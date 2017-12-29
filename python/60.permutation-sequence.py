#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence
#
# Medium (28.08%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '1\n1'
#
# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
#
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.
#


class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ret = ""
        table = [i for i in xrange(1, n + 1)]
        f = [1 for _ in xrange(0, n + 1)]
        # Calculate n! and save to array.
        for i in xrange(1, n + 1):
            f[i] = f[i - 1] * i
        k = k - 1
        for i in xrange(n, 0, -1):
            index = k / f[i - 1]
            ret = ret + str(table[index])
            del table[index]
            k = k % f[i - 1]
        return ret
