#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (39.87%)
# Total Accepted:    258.5K
# Total Submissions: 648.3K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#
#


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        roundup = True
        i = len(digits)-1
        while roundup and i >= 0:
            if digits[i] == 9:
                roundup = True
                digits[i] = 0
            else:
                roundup = False
                digits[i] += 1
            i -= 1
        if roundup:
            digits.insert(0, 1)
        return digits
