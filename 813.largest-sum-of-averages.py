#
# [831] Largest Sum of Averages
#
# https://leetcode.com/problems/largest-sum-of-averages/description/
#
# algorithms
# Medium (40.11%)
# Total Accepted:    3.3K
# Total Submissions: 8.3K
# Testcase Example:  '[9,1,2,3,9]\n3'
#
# We partition a row of numbers A into at most K adjacent (non-empty) groups,
# then our score is the sum of the average of each group. What is the largest
# score we can achieve?
#
# Note that our partition must use every number in A, and that scores are not
# necessarily integers.
#
#
# Example:
# Input:
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation:
# The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 +
# (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 100.
# 1 <= A[i] <= 10000.
# 1 <= K <= A.length.
# Answers within 10^-6 of the correct answer will be accepted as correct.
#
#
#


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        dp = [0]*len(A)
        for i in xrange(len(A)):
            dp[i] = sum(A[:i+1])/float(i+1)
        for k in xrange(K-1):
            for j in xrange(len(A)-1, k, -1):
                for i in xrange(0, j):
                    dp[j] = max(dp[j], dp[i]+sum(A[i+1:j+1])/float(j-i))
        return dp[-1]
