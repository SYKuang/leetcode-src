#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (36.91%)
# Total Accepted:    242.3K
# Total Submissions: 656K
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
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
        if not digits:
            return []
        table = [[], [], ["a", "b", "c"],  ["d", "e", "f"],  ["g", "h", "i"], ["j", "k", "l"],  [
            "m", "n", "o"],  ["p", "q", "r", "s"],  ["t", "u", "v"],  ["w", "x", "y", "z"]]
        res = [""]
        for d in digits:
            tmp = []
            for pre in res:
                for post in table[int(d)]:
                    tmp.append(pre+post)
            res = tmp
        return res
