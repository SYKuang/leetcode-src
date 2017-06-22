#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title
#
# Easy (25.31%)
# Total Accepted:    100195
# Total Submissions: 393173
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases.
#
class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ""
        if n == 0:
            return 0
        while n > 0:
            if n % 26 == 0:
                ret = "Z" + ret
                n = n -26
            else:
                ret = chr(ord('A') + n % 26 - 1) + ret
            n = n / 26
        return ret

