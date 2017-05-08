#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
#
# Medium (33.63%)
# Total Accepted:    147423
# Total Submissions: 435252
# Testcase Example:  '""'
#
# Given a digit string, return all possible letter combinations that the number
# could represent.
# 
# 
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below.
# 
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        res=[]
        for i in xrange(len(digits)):
            tmpRes=[]
            chars=self.getChars(digits[i])
            for char in chars:
                for lastRes in res:
                    tmpRes.append(lastRes+char)
            if len(tmpRes)==0:
                res=chars
            else:
                res=tmpRes
        return res
    def getPre(self,strs):
        if len(strs)==1:
            return self.getChars(strs)
        res=[]
        lastRes=self.getPre(strs[1:])
        for char in self.getChars(strs[0]):
            for lastStr in lastRes:
                res.append(char+lastStr)
        return res
    def getChars(self,digit):
        return{
            "1":["*"],
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "0":[" "],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }[digit]
