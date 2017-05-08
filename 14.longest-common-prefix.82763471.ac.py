#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix
#
# Easy (31.16%)
# Total Accepted:    173968
# Total Submissions: 556068
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        ans=strs[0]
        for i in range(0,len(strs[0])):
       
            bAllSame = True
            for str in strs:
                if len(str) <= i:
                    bAllSame=False
                    break
                elif str[i] != strs[0][i]:
                    bAllSame=False
                    break
            
            if bAllSame is False:
                #print i
                if i==0:
                    return ""
                elif i==1:
                    return strs[0][0]
                else:

                #print strs[0][0:1]
                    ans=strs[0][0:i]
                    break

        return ans
