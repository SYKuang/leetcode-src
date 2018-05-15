#
# [358] Rearrange String k Distance Apart
#
# https://leetcode.com/problems/rearrange-string-k-distance-apart/description/
#
# algorithms
# Hard (31.61%)
# Total Accepted:    14.8K
# Total Submissions: 46.7K
# Testcase Example:  '"aabbcc"\n3'
#
#
# Given a non-empty string s and an integer k, rearrange the string such that
# the same characters are at least distance k from each other.
#
#
# All input strings are given in lowercase letters. If it is not possible to
# rearrange the string, return an empty string "".
#
# Example 1:
#
# s = "aabbcc", k = 3
#
# Result: "abcabc"
#
# The same letters are at least distance 3 from each other.
#
#
#
# Example 2:
#
# s = "aaabc", k = 3
#
# Answer: ""
#
# It is not possible to rearrange the string.
#
#
#
# Example 3:
#
# s = "aaadbbcc", k = 2
#
# Answer: "abacabcd"
#
# Another possible answer is: "abcabcda"
#
# The same letters are at least distance 2 from each other.
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        l = len(s)
        if k == 0:
            return s
        table = collections.defaultdict(int)
        for c in s:
            table[c] += 1
        arr = [(table[c], c) for c in table]
        arr.sort(reverse=True)
        maxLen = arr[0][0]
        group = [[] for _ in xrange(maxLen)]
        i = 0
        for cnt, c in arr:
            for _ in xrange(cnt):
                group[i].append(c)
                i = (i+1) % max(cnt, maxLen-1)
        for word in group[:-1]:
            if len(word) < k:
                return ""
        return "".join(map(lambda x: "".join(x), group))


# Time limit excceed
class Solution2(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        l = len(s)
        if k == 0:
            return s
        table = collections.defaultdict(int)
        for c in s:
            table[c] += 1
        q = []
        for c in table:
            heapq.heappush(q, (-table[c], c))
        ret = ""
        while q:
            cnt = min(k, l)
            tq = []
            for _ in xrange(cnt):
                if not q:
                    return ""
                feq, c = heapq.heappop(q)
                feq += 1
                ret += c
                if feq < 0:
                    tq.append((feq, c))
                l -= 1
            for d in tq:
                heapq.heappush(q, d)
        return ret
