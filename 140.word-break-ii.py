#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (24.71%)
# Total Accepted:    115.4K
# Total Submissions: 467.1K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#
#


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        totalword = set([c for w in wordDict for c in w])
        for c in s:
            if c not in totalword:
                return []
        self.table = {}
        return self.helper(s, wordDict)

    def helper(self, s, wordDict):
        if s == "":
            return []
        if s in self.table:
            return self.table[s]
        ret = []
        for w in wordDict:
            if s[:len(w)] == w:
                rest = s[len(w):]
                if rest == "":
                    ret.append(w)
                else:
                    tmp = self.helper(s[len(w):], wordDict)
                    for t in tmp:
                        ret.append(s[:len(w)]+" "+t)
        self.table[s] = ret
        return ret
