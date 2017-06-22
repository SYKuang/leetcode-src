#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number
#
# Easy (46.28%)
# Total Accepted:    128497
# Total Submissions: 276267
# Testcase Example:  '"A"'
#
# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):

        def titleToNumber(self, s):
            """
            :type s: str
            :rtype: int
            """
            bitCount = 1
            ret = 0
            for i in range(len(s)-1, -1, -1):
                ret = ret + (ord(s[i]) - ord('A') + 1) * bitCount
                bitCount = bitCount * 26
            return ret

