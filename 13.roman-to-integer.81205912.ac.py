#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer
#
# Easy (44.81%)
# Total Accepted:    148797
# Total Submissions: 330372
# Testcase Example:  '"DCXXI"'
#
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
def switch(x):
    return{
        'I':1,
        'C':100,
        'V':5,
        'X':10,
        'D':500,
        'M':1000,
        'L':50,
    }[x]
class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i=0
        current=switch(s[i])
        while i < len(s)-1:
            nextc=switch(s[i+1])
            
            if  current >= nextc:
                res += current
            else:
                res -= current
            i += 1
            current = nextc
        res += switch(s[len(s)-1])
        return res
            
