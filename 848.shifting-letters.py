#
# [878] Shifting Letters
#
# https://leetcode.com/problems/shifting-letters/description/
#
# algorithms
# Medium (33.78%)
# Total Accepted:    3.8K
# Total Submissions: 11.3K
# Testcase Example:  '"abc"\n[3,5,9]'
#
# We have a string S of lowercase letters, and an integer array shifts.
#
# Call the shift of a letter, the next letter in the alphabet, (wrapping around
# so that 'z' becomes 'a'). 
#
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
#
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x
# times.
#
# Return the final string after all such shifts to S are applied.
#
# Example 1:
#
#
# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation:
# We start with "abc".
# After shifting the first 1 letters of S by 3, we have "dbc".
# After shifting the first 2 letters of S by 5, we have "igc".
# After shifting the first 3 letters of S by 9, we have "rpl", the answer.
#
#
# Note:
#
#
# 1 <= S.length = shifts.length <= 20000
# 0 <= shifts[i] <= 10 ^ 9
#
#


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        n = len(shifts)
        sums = [0]*n
        count = 0
        for i in xrange(n-1, -1, -1):
            count += shifts[i]
            sums[i] = count
        s = [c for c in S]
        for i in xrange(len(s)):
            s[i] = chr(((ord(s[i])-ord('a')+sums[i]) % 26)+ord('a'))
        return "".join(s)
