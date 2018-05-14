#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (26.55%)
# Total Accepted:    41.1K
# Total Submissions: 155K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language which uses the latin alphabet. However, the
# order among letters are unknown to you. You receive a list of non-empty words
# from the dictionary, where words are sorted lexicographically by the rules of
# this new language. Derive the order of letters in this language.
#
# Example 1:
#
#
# Input:
# [
# ⁠ "wrt",
# ⁠ "wrf",
# ⁠ "er",
# ⁠ "ett",
# ⁠ "rftt"
# ]
#
# Output: "wertf"
#
#
# Example 2:
#
#
# Input:
# [
# ⁠ "z",
# ⁠ "x"
# ]
#
# Output: "zx"
#
#
# Example 3:
#
#
# Input:
# [
# ⁠ "z",
# ⁠ "x",
# ⁠ "z"
# ]
#
# Output: "" 
#
# Explanation: The order is invalid, so return "".
#
#
# Note:
#
#
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the
# given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is
# fine.
#
#
#


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        """
        Similar to 444 sequence-reconstruction.
        Create the topological graph of words(Compare between 2 words rather
        than the character of word).
        After that use bfs to travel topological graph.
        """
        indgree = {}
        subsect = collections.defaultdict(set)
        for word in words:
            for c in word:
                indgree[c] = 0
        for c, n in zip(words, words[1:]):
            l = min(len(c), len(n))
            for i in xrange(l):
                if c[i] != n[i]:
                    if n[i] not in subsect[c[i]]:
                        indgree[n[i]] += 1
                        subsect[c[i]].add(n[i])
                    break

        q = [i for i in indgree.keys() if indgree[i] == 0]
        ret = ""
        while q:
            t = q[0]
            del q[0]
            for c in subsect[t]:
                indgree[c] -= 1
                if indgree[c] == 0:
                    q.append(c)
            ret += t
        if len(ret) != len(indgree):
            return ""
        return ret
