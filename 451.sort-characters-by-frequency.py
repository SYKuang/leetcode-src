#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (52.05%)
# Total Accepted:    55.5K
# Total Submissions: 106.6K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
#
#
#
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
#
#
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
#
#


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = collections.defaultdict(int)
        for c in s:
            table[c] += 1
        q = []
        for k in table:
            heapq.heappush(q, (-table[k], k))
        res = []
        while q:
            count, char = heapq.heappop(q)
            count = -count
            res += [char]*count
        return "".join(res)
