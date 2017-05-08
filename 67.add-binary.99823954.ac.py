#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary
#
# Easy (31.53%)
# Total Accepted:    140430
# Total Submissions: 442007
# Testcase Example:  '"0"\n"0"'
#
# 
# Given two binary strings, return their sum (also a binary string).
# 
# 
# 
# For example,
# a = "11"
# b = "1"
# Return "100".
# 
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        indexA = len(a)-1
        indexB = len(b)-1
        Sum = ""
        carries =0
        while indexA >=0 or indexB >=0:
            x = int(a[indexA]) if indexA >=0 else 0
            y = int(b[indexB]) if indexB >=0 else 0
            Sum = str((x+y+carries)%2) + Sum
            if x+y+carries>=2:
                carries = 1
            else:
                carries =0
            indexA ,indexB = indexA-1 ,indexB-1
        if carries != 0:
            Sum = "1" + Sum
        return Sum
        
