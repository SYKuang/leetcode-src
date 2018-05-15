#
# [527] Word Abbreviation
#
# https://leetcode.com/problems/word-abbreviation/description/
#
# algorithms
# Hard (43.97%)
# Total Accepted:    5.4K
# Total Submissions: 12.4K
# Testcase Example:  '["like","god","internal","me","internet","interval","intension","face","intrusion"]'
#
# Given an array of n distinct non-empty strings, you need to generate minimal
# possible abbreviations for every word following rules below.
#
#
# Begin with the first character and then the number of characters abbreviated,
# which followed by the last character.
# If there are any conflict, that is more than one words share the same
# abbreviation, a longer prefix is used instead of only the first character
# until making the map from word to abbreviation become unique. In other words,
# a final abbreviation cannot map to more than one original words.
# ⁠If the abbreviation doesn't make the word shorter, then keep it as
# original.
#
#
# Example:
#
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension",
# "face", "intrusion"]
# Output:
# ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
#
#
#
#
# Note:
#
# ⁠Both n and the length of each word will not exceed 400.
# ⁠The length of each word is greater than 1.
# ⁠The words consist of lowercase English letters only.
# ⁠The return answers should be in the same order as the original array.
#
#


class Solution(object):
    def wordsAbbreviation(self, dicts):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        ret = []
        l = len(dicts)
        pre = [1]*l
        for i in xrange(l):
            ret.append(self.abbreviate(dicts[i], pre[i]))
        for i in xrange(l):
            while True:
                s = set()
                for j in xrange(i+1, l):
                    if ret[i] == ret[j]:
                        s.add(j)
                if not s:
                    break
                s.add(i)
                for j in s:
                    pre[j] += 1
                    ret[j] = self.abbreviate(dicts[j], pre[j])
        return ret

    def abbreviate(self, word, k):
        l = len(word)
        if k >= l-2:
            return word
        return word[:k]+str(l-k-1)+word[-1:]
