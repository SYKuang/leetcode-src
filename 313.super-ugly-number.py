#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (38.46%)
# Total Accepted:    47.4K
# Total Submissions: 123.3K
# Testcase Example:  '12\n[2,7,13,19]'
#
# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
#
# Example:
#
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12
# ⁠            super ugly numbers given primes = [2,7,13,19] of size 4.
#
# Note:
#
#
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
#
#
#


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        idx = [0]*len(primes)
        while len(res) < n:
            tmp = []
            for i in xrange(len(primes)):
                tmp.append(res[idx[i]]*primes[i])
            mn = min(tmp)
            for i in xrange(len(primes)):
                if res[idx[i]]*primes[i] == mn:
                    idx[i] += 1
            res.append(mn)

        return res[-1]
