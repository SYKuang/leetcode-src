#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle
#
# Easy (37.71%)
# Total Accepted:    128603
# Total Submissions: 338872
# Testcase Example:  '0'
#
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# 
# For example, given numRows = 5,
# Return
# 
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        Ret=list()
        for i in range(1,numRows+1):
            row=list()
            for j in range(1,i+1):
                if 1==j or i==j:
                    row.append(1)
                else:
                    
                    row.append(Ret[i-2][j-1]+Ret[i-2][j-2])
            Ret.append(row)
        return Ret
