#
# [651] 4 Keys Keyboard
#
# https://leetcode.com/problems/4-keys-keyboard/description/
#
# algorithms
# Medium (49.49%)
# Total Accepted:    8.1K
# Total Submissions: 16.4K
# Testcase Example:  '1'
#
# Imagine you have a special keyboard with the following keys:
# Key 1: (A):  Print one 'A' on screen.
# Key 2: (Ctrl-A): Select the whole screen.
# Key 3: (Ctrl-C): Copy selection to buffer.
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already
# been printed.
#
#
#
# Now, you can only press the keyboard for N times (with the above four keys),
# find out the maximum numbers of 'A' you can print on screen.
#
#
# Example 1:
#
# Input: N = 3
# Output: 3
# Explanation:
# We can at most get 3 A's on screen by pressing following key sequence:
# A, A, A
#
#
#
# Example 2:
#
# Input: N = 7
# Output: 9
# Explanation:
# We can at most get 9 A's on screen by pressing following key sequence:
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
#
#
#
# Note:
#
# 1
# Answers will be in the range of 32-bit signed integer.
#
#
#
#


class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 4:
            return N
        dp = [0]*(N+1)
        for i in xrange(1, 5):
            dp[i] = i
        for i in xrange(5, N+1):
            dp[i] = max(dp[i-1]+1, dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
        return dp[N]
