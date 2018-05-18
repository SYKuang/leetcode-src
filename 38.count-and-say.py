#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (36.95%)
# Total Accepted:    194.1K
# Total Submissions: 525.1K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
#
#
# Given an integer n, generate the nth term of the count-and-say sequence.
#
#
#
# Note: Each term of the sequence of integers will be represented as a
# string.
#
#
# Example 1:
#
# Input: 1
# Output: "1"
#
#
#
# Example 2:
#
# Input: 4
# Output: "1211"
#
#
#


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        '''
        Recursive version
        pre = self.countAndSay(n-1)+"*"
        ret = ""
        count = 1
        for a, b in zip(pre[:-1], pre[1:]):
            if a == b:
                count += 1
            else:
                ret += str(count)+a
                count = 1
        return ret
        '''
        ret = "1"
        for _ in xrange(1, n):
            new = ""
            ret += "*"
            count = 1
            for a, b in zip(ret[:-1], ret[1:]):
                if a == b:
                    count += 1
                else:
                    new += str(count)+a
                    count = 1
            ret = new
        return ret
