#
# [249] Group Shifted Strings
#
# https://leetcode.com/problems/group-shifted-strings/description/
#
# algorithms
# Medium (44.54%)
# Total Accepted:    34.4K
# Total Submissions: 77.3K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the
# sequence:
#
#
# "abc" -> "bcd" -> ... -> "xyz"
#
# Given a list of strings which contains only lowercase alphabets, group all
# strings that belong to the same shifting sequence.
#
# Example:
#
#
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output:
# [
# ⁠ ["abc","bcd","xyz"],
# ⁠ ["az","ba"],
# ⁠ ["acef"],
# ⁠ ["a","z"]
# ]
#
#
#


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        group = collections.defaultdict(list)
        for s in strings:
            base = ord(s[0])
            rule = 0
            for c in s:
                rule += (ord(c) - base) % 26
                rule *= 26
            group[(len(s), rule)].append(s)
        ret = [x for x in group.values()]
        return ret
