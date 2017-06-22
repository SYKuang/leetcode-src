#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion
#
# Medium (26.43%)
# Total Accepted:    151718
# Total Submissions: 571197
# Testcase Example:  '""\n1'
#
# 
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# string convert(string text, int nRows);
# 
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# 
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr=[]
        if len(s)<=numRows or numRows == 1:
            return s
        for i in range(0,numRows):
            arr.append("")


            
        for i in range(0,len(s)):
            if numRows==2:
                arr[i%2]+=s[i]
            else:
                pi=(i+1)%(numRows*2-2)
                #print pi
                if pi <= numRows and pi != 0:
                    arr[pi-1]+=s[i]
                else:
                    if pi == 0:
                        pi=(numRows*2-2)
                    arr[numRows-(pi-numRows)-1]+=s[i]
        res=""
        #print arr
        for i in range(0,numRows):
            res+=arr[i]
        return res
