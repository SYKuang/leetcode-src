#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (33.79%)
# Total Accepted:    98K
# Total Submissions: 289.9K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
#
# Example:
#
#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had
# ⁠            received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining
# two with no more than 3 citations each, his h-index is 3.
#
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
#
#

# O(n) use bucket sort


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        bucket = [0] * (n + 1)
        for c in citations:
            if c > n:
                c = n
            bucket[c] += 1
        count = 0
        while n >= 0: # Reuse n as index
            count += bucket[n]
            h_index = n
            if count >= h_index:
                return h_index
            n -= 1
# Beats 50%, time complexity is O(nlogn)


class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if not n:
            return 0
        citations.sort()
        ret = 0
        for i in xrange(n):
           h = n - i
           if citations[i] >= h and i <= n - h:
               ret = h
               break
        return ret
