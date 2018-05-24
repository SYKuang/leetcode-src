#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (39.09%)
# Total Accepted:    203.4K
# Total Submissions: 520.4K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# Note:
#
#
# All inputs will be in lowercase.
# The order of your output does not matter.
#
#
#


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = collections.defaultdict(list)
        for s in strs:
            count = collections.defaultdict(int)
            for c in s:
                count[c] += 1
            skey = ""
            for k in sorted(count.keys()):
                c = count[k]
                skey += str(c) + k
            table[skey].append(s)
        return table.values()
