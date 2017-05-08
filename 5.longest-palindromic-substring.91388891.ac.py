#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring
#
# Medium (25.09%)
# Total Accepted:    201543
# Total Submissions: 802344
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example:
# 
# Input: "babad"
# 
# Output: "bab"
# 
# Note: "aba" is also a valid answer.
# 
# 
# 
# Example:
# 
# Input: "cbbd"
# 
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        maxright=0
        pos=0
        preS='#'+'#'.join(s)+'#'

        p=[0]*len(preS)

        maxlen = 0
        maxCent = 0
        for i in xrange(len(preS)):
            if i >= maxright:
                p[i]=1
            else:
                p[i]=min(p[pos-(i-pos)],maxright-i)
            while i+p[i] < len(preS) and i-p[i] >=0 and preS[i+p[i]] == preS[i-p[i]]:
                p[i]+=1
            
            if p[i]+i > maxright:
                maxright = p[i]+i
                pos = i

            if p[i] > maxlen:
                maxlen=p[i]
                maxCent=i

        return s[(maxCent-maxlen+1)/2:(maxCent-maxlen+1)/2+maxlen-1]
        
        
                    

                            
    def preProcessStr(self,s):
        newS=[]
        for i in xrange(len(s)):
            newS.append(s)
            newS.append("#")
        return newS
