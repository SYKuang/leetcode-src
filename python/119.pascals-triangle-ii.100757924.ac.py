#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii
#
# Easy (35.98%)
# Total Accepted:    113243
# Total Submissions: 312737
# Testcase Example:  '0'
#
# Given an index k, return the kth row of the Pascal's triangle.
# 
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# 
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution(object):
    def getRow(self, rowIndex):
        array = [1]*(rowIndex+1)

        for i in range(1,rowIndex+1):
            for j in range(i-1,0,-1):
                array[j] += array[j-1]

        return array
