#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (30.49%)
# Total Accepted:    30.2K
# Total Submissions: 99.2K
# Testcase Example:  '8'
#
#
# Given a positive integer n and you can do operations as follow:
#
#
#
#
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
#
#
#
#
# What is the minimum number of replacements needed for n to become 1?
#
#
#
#
# Example 1:
#
# Input:
# 8
#
# Output:
# 3
#
# Explanation:
# 8 -> 4 -> 2 -> 1
#
#
#
# Example 2:
#
# Input:
# 7
#
# Output:
# 4
#
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
#
#
#


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 1:
            if n == 3:
                count += 2
                break
            if n % 4 == 1:
                n -= 1
            elif n % 4 == 3:
                n += 1
            else:
                n /= 2
            count += 1
        return count
