#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways
#
# Medium (19.39%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '""'
#
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
#
# Given an encoded message containing digits, determine the total number of
# ways to decode it.
#
#
#
# For example,
# Given encoded message "12",
# it could be decoded as "AB" (1 2) or "L" (12).
#
#
#
# The number of ways decoding "12" is 2.
#
#


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0

        dp = [0 for _ in xrange(len(s) + 1)]
        dp[0] = dp[1] = 1
        for i in xrange(1, len(s)):
            v = int(s[i - 1:i + 1])
            if v <= 26 and v > 9:
                dp[i + 1] = dp[i + 1] + dp[i - 1]
            if s[i] != '0':
                dp[i + 1] = dp[i + 1] + dp[i]
        return dp[len(s)]
