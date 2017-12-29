#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code
#
# algorithms
# Medium (41.52%)
# Total Accepted:    97.9K
# Total Submissions: 235.1K
# Testcase Example:  '0'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
#
# Note:
# For a given n, a gray code sequence is not uniquely defined.
#
# For example, [0,2,3,1] is also a valid gray code sequence according to the
# above definition.
#
# For now, the judge is able to judge based on one instance of gray code
# sequence. Sorry about that.
#


class Solution(object):

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0]
        inc = 1
        for i in xrange(n):
            length = len(ret)
            for j in xrange(length-1, -1, -1):
                ret.append(ret[j] + inc)
            inc = inc << 1
        return ret
