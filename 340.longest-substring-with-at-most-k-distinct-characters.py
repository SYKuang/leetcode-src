#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Hard (38.40%)
# Total Accepted:    40.7K
# Total Submissions: 106K
# Testcase Example:  '"eceba"\n2'
#
#
# Given a string, find the length of the longest substring T that contains at
# most k distinct characters.
#
#
#
# For example,
#
# Given s = “eceba” and k = 2,
#
#
#
# T is "ece" which its length is 3.
#
#


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if k == 0:
            return 0
        if len(s) <= k:
            return len(s)
        table = {}
        ret = 0
        start = 0
        for i, c in enumerate(s):
            table[c] = i
            if len(table) > k:
                ret = max(ret, i-start)
                start = min(table.values())
                del table[s[start]]
                start += 1
        return max(ret, len(s)-start)
