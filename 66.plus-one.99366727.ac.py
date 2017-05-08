#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one
#
# Easy (37.88%)
# Total Accepted:    166823
# Total Submissions: 437744
# Testcase Example:  '[0]'
#
# Given a non-negative integer represented as a non-empty array of digits, plus
# one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        RoundUp = False
        index = len(digits)-1
        if (digits[index] + 1) %10 < digits[index]:
            RoundUp = True
        digits[index] = (digits[index] + 1) % 10
        index = index -1
        while RoundUp and index >=0:
            if (digits[index] + 1) %10 < digits[index]:
                RoundUp = True
            else:
                RoundUp = False
            digits[index] = (digits[index] + 1) % 10
            index = index -1
        if RoundUp:
            digits.insert(0,1)
        return digits
        
        
