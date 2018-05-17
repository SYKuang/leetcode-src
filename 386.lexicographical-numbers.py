#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (42.42%)
# Total Accepted:    29K
# Total Submissions: 68.3K
# Testcase Example:  '13'
#
#
# Given an integer n, return 1 - n in lexicographical order.
#
#
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
#
#
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
#
#


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = range(n)
        cur = 1
        for i in xrange(n):
            ret[i] = cur
            if cur*10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur /= 10
                cur += 1
                while cur % 10 == 0:
                    cur /= 10
        return ret
