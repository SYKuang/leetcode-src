#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr
#
# Easy (27.58%)
# Total Accepted:    180367
# Total Submissions: 650515
# Testcase Example:  '""\n""'
#
# 
# Implement strStr().
# 
# 
# Returns the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) ==0:
            return -1
        for i in xrange(len(haystack)):
            if len(haystack)-i < len(needle):
                return -1
            if haystack[i] == needle[0]:
                same=True
                for j in xrange(1,len(needle)):
                    if haystack[i+j] != needle[j]:
                        same=False
                        break
                if same:
                    return i
        return -1
