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
        d = collections.defaultdict(list)
        for word in words:
            d[word[0]].append(word)
        m = len(words)
        for i, c in enumerate(S):
            if m == 0:
                break
            u = d[c]
            d[c] = []
            for word in u:
                word = word[1:]
                if not word:
                    m -= 1
                    continue
                d[word[0]].append(word)
        return len(words)-m
