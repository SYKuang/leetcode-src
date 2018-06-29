#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (51.46%)
# Total Accepted:    9.5K
# Total Submissions: 18.4K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to
# make two strings equal.
#
# Example 1:
#
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
#
#
#
# Example 2:
#
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e]
# to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
#
#
#
# Note:
# 0 < s1.length, s2.length .
# All elements of each string will have an ASCII value in [97, 122].
#
#


class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if not s1:
            return sum([ord(c) for c in s2])
        if not s2:
            return sum([ord(c) for c in s1])
        dp = [0]*(len(s2)+1)
        for i in xrange(1, len(s2)+1):
            dp[i] = dp[i-1]+ord(s2[i-1])
        for i in xrange(1, len(s1)+1):
            t1 = dp[0]
            dp[0] += ord(s1[i-1])
            for j in xrange(1, len(s2)+1):
                t2 = dp[j]
                dp[j] = t1 if s2[j-1] == s1[i -
                                            1] else min(dp[j-1]+ord(s2[j-1]), dp[j]+ord(s1[i-1]))
                t1 = t2
        return dp[-1]
