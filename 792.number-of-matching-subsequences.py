#
# [808] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (36.25%)
# Total Accepted:    6.7K
# Total Submissions: 18.3K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
#
#
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
#
#
# Note:
#
#
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
#
#


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def isSubseq(S, word):
            index = 0
            for c in word:
                index = S.find(c, index)
                if index == -1:
                    return False
                index += 1
            return True
        res = 0
        for word in words:
            if isSubseq(S, word):
                res += 1
        return res
