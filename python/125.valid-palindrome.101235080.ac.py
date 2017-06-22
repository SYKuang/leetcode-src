#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome
#
# Easy (25.87%)
# Total Accepted:    158678
# Total Submissions: 611392
# Testcase Example:  '""'
#
# 
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# 
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# 
# 
# Note:
# Have you consider that the string might be empty? This is a good question to
# ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
# 
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=re.sub(r'\W+','',s)
        s=s.lower()
        for i in range(0,len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
            
