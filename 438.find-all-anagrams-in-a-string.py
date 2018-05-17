#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (33.94%)
# Total Accepted:    63.5K
# Total Submissions: 187K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l = len(p)
        sl = len(s)
        if len(s) < l:
            return []
        table = collections.defaultdict(int)
        for c in p:
            table[c] += 1
        ret = []
        right, left, count = (0, 0, l)
        # Sliding window template
        while right < sl:
            # 1. Enlarge Window if current element in target.
            if table[s[right]] > 0:
                count -= 1
            table[s[right]] -= 1
            right += 1
            # 2. According to count or other condition to determine if it's fit
            # target or not
            if count == 0:
                ret.append(left)
            # 3. As long as there is a possible solution, decrease the windows.
            if right-left == l:
                if table[s[left]] >= 0:
                    count += 1
                table[s[left]] += 1
                left += 1

        return ret
