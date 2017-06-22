#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say
#
# Easy (33.65%)
# Total Accepted:    133490
# Total Submissions: 394303
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# 
# 
# Given an integer n, generate the nth sequence.
# 
# 
# 
# Note: The sequence of integers will be represented as a string.
# 
# 
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n==0:
            return ""
        elif n==1:
            return "1"
        res="1"
        for i in xrange(1,n):
            newRes=""
            index=0
            while index < len(res):
                count = 1
                
                if index == len(res)-1:
                    newRes+=str(count)
                    newRes+=str(res[index])
                    
                    break
                while res[index+1]==res[index]:
                    count +=1
                    index +=1
                    
                    if index >= len(res)-1:
                        break
                newRes+=str(count)
                newRes+=str(res[index])
                index+=1
            
            res=newRes
        return res
            
