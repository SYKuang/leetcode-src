#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (27.01%)
# Total Accepted:    149.2K
# Total Submissions: 552.2K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
#
#
#


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = len(s)
        lt = len(t)
        if ls < lt:
            return ""
        table = collections.defaultdict(int)
        for c in t:
            table[c] += 1
        left = 0
        right = 0
        count = 0
        ret = ""
        while right < ls:
            if table[s[right]] > 0:
                count += 1
            if count == lt:
                while left < right and table[s[left]] < 0:
                    table[s[left]] += 1
                    left += 1
                ret = s[left:right+1]
            table[s[right]] -= 1
            if ret != "":
                if table[s[left]] >= 0:
                    count -= 1
                table[s[left]] += 1
                left += 1
            right += 1
        return ret
