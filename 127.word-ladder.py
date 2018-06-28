#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (20.40%)
# Total Accepted:    172.1K
# Total Submissions: 841.9K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#


class Solution(object):
    def __init__(self):
        self.table = {}

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)

        def getNeibor(word):
            res = []
            for i in xrange(len(word)):
                for letter in string.ascii_lowercase:
                    w = word[:i]+letter+word[i+1:]
                    if w in wordList:
                        res.append(w)
            return res
        q = collections.deque([(beginWord, 1)])
        seen = set([beginWord])
        while q:
            item = q.popleft()
            for neibor in getNeibor(item[0]):
                if neibor == endWord:
                    return item[1]+1
                if neibor in seen:
                    continue
                seen.add(neibor)
                q.append((neibor, item[1]+1))
        return 0
