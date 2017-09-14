#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams
#
# Medium (33.81%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
#
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
# ⁠ ["ate", "eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# Note: All inputs will be in lower-case.
#


class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = dict()
        for i, s in enumerate(strs):
            key = str(sorted(s))
            if key in table:
                table[key].append(i)
            else:
                table[key] = [i]
        ret = []
        for key in table:
            ret.append([strs[table[key][0]]])
            for i in xrange(1, len(table[key])):
                ret[-1].append(strs[table[key][i]])
        return ret
