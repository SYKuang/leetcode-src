#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (40.82%)
# Total Accepted:    129.9K
# Total Submissions: 318K
# Testcase Example:  '27'
#
# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
#
# Input: 27
# Output: true
#
#
# Example 2:
#
#
# Input: 0
# Output: false
#
# Example 3:
#
#
# Input: 9
# Output: true
#
# Example 4:
#
#
# Input: 45
# Output: false
#
# Follow up:
# Could you do it without using any loop / recursion?
#
#


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n < 1 else 3**19 % n == 0
