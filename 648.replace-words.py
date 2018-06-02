#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (48.32%)
# Total Accepted:    17.8K
# Total Submissions: 36.9K
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
#
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
#
#
#
#
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
#
#
#
# You need to output the sentence after the replacement.
#
#
#
# Example 1:
#
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
#
#
#
#
# Note:
#
# The input will only have lower-case letters.
# ⁠1
# ⁠1
# ⁠1
# ⁠1
#
#
#


class Solution(object):
    def replaceWords(self, dicts, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if not dicts or not sentence:
            return sentence
        dicts.sort()
        pre = dicts[0]+"z"
        duplicate = set()
        for word in dicts:
            if len(pre) < len(word) and word[:len(pre)] == pre:
                duplicate.add(word)
            else:
                pre = word
        dicts = [d for d in dicts if d not in duplicate]
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            j = bisect.bisect_right(dicts, word)
            root = dicts[max(j-1, 0)]
            if root == word[:len(root)]:
                sentence[i] = root
        return " ".join(sentence)


# Beats 15%


class Solution2(object):
    def replaceWords(self, dicts, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if not dicts or not sentence:
            return sentence
        sentence = sentence.split()
        res = []
        dicts = set(dicts)
        for word in sentence:
            for i in xrange(1, len(sentence)):
                w = word[:i]
                if w in dicts:
                    word = w
                    break
            res.append(word)
        return " ".join(res)
