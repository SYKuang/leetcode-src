#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (32.63%)
# Total Accepted:    30.9K
# Total Submissions: 94.8K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
#
#
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
#
#
# Example:
# Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes
# you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
#
#


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        dp = []
        envelopes.sort(cmp=lambda x, y: x[0]-y[0] if x[0] != y[0] else y[1]-x[1])
        for i in xrange(len(envelopes)):
            index = bisect.bisect_left(dp, envelopes[i][1])
            if index < len(dp):
                dp[index] = envelopes[i][1]
            else:
                dp.append(envelopes[i][1])
        return len(dp)
