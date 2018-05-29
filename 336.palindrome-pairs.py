#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (27.29%)
# Total Accepted:    39.6K
# Total Submissions: 145K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
#
# ⁠   Given a list of unique words, find all pairs of distinct indices (i, j)
# in the given list, so that the concatenation of the two words, i.e. words[i]
# + words[j] is a palindrome.
#
#
#
# ⁠   Example 1:
# ⁠   Given words = ["bat", "tab", "cat"]
# ⁠   Return [[0, 1], [1, 0]]
# ⁠   The palindromes are ["battab", "tabbat"]
#
#
# ⁠   Example 2:
# ⁠   Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# ⁠   Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# ⁠   The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


def isPalindrom(word):
    return True if word == word[::-1] else False


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dicts = {}
        for i, w in enumerate(words):
            dicts[w[::-1]] = i
        ret = []
        for i, w in enumerate(words):
            for j in xrange(len(w)+1):
                l = w[:j]
                r = w[j:]
                if l in dicts and dicts[l] != i and isPalindrom(r):
                    ret.append([i, dicts[l]])
                if j > 0 and r in dicts and dicts[r] != i and isPalindrom(l):
                    ret.append([dicts[r], i])
        return ret

# Trie


class Node(object):
    def __init__(self):
        self.index = []
        self.child = {}
        self.val = -1


class Trie(object):
    def __init__(self):
        self.root = Node()

    def add(self, index, word):
        node = self.root
        for i, c in enumerate(word):
            if c not in node.child:
                node.child[c] = Node()
            if i != len(word) and isPalindrom(word[i:]):
                node.index.append(index)
            node = node.child[c]
        node.val = index
        node.index.append(index)


class Solution2(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        tree = Trie()

        for i, word in enumerate(words):
            tree.add(i, word[::-1])
        ret = []
        for i, word in enumerate(words):
            root = tree.root
            find = True
            for j, c in enumerate(word):
                if isPalindrom(word[j:]) and root.val != -1 and root.val != i:
                    ret.append([i, root.val])
                if c in root.child:
                    root = root.child[c]
                else:
                    find = False
                    break
            if find:
                for index in root.index:
                    if index != i:
                        ret.append([i, index])
        return ret
