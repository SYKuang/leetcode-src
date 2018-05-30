#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (18.21%)
# Total Accepted:    65.9K
# Total Submissions: 361.8K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
#
# Example 1:
#
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
#
# Example 2:
#
#
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
#
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
#
#
#


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        num = numerator
        den = denominator
        if num*den < 0:
            negtive = True
        else:
            negtive = False
        num = abs(num)
        den = abs(den)
        res = "-" if negtive else ""
        res += str(num//den)
        num = num % den
        if num:
            table = {}
            i = 0
            table[num] = i
            frac = ""
            while num:
                num *= 10
                frac += str(num/den)
                num = num % den
                if num in table:
                    frac = frac[:table[num]]+"("+frac[table[num]:] + ")"
                    break
                i += 1
                table[num] = i
            res+="."+frac if frac else res
        return res
