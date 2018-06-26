#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (30.57%)
# Total Accepted:    41.2K
# Total Submissions: 134.8K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
#
# Example 1:
#
#
# Input: "bcabc"
# Output: "abc"
#
#
# Example 2:
#
#
# Input: "cbacdcbc"
# Output: "acdb"
#
#
#


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = collections.defaultdict(int)
        for c in s:
            table[c] += 1
        res = []
        visited = set()
        for c in s:
            table[c] -= 1
            if c in visited:
                continue
            while res and c < res[-1] and table[res[-1]]:
                visited.remove(res[-1])
                res.pop()
            res.append(c)
            visited.add(c)
        return "".join(res)
