#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (28.14%)
# Total Accepted:    140.4K
# Total Submissions: 499K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
# Example 1:
#
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
#
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Note:
#
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#
#
#


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = ["0"]*(len(num1)+len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in xrange(len(num1)):
            carry = 0
            for j in xrange(len(num2)):
                carry += (int(num1[i])*int(num2[j]))+int(ret[i+j])
                ret[i+j] = str(carry % 10)
                carry /= 10
            if carry:
                ret[len(num2)+i] = str(carry)
        while len(ret) > 1 and ret[-1] == "0":
            ret.pop()
        return "".join(ret[::-1])
