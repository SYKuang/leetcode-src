#
# [276] Paint Fence
#
# https://leetcode.com/problems/paint-fence/description/
#
# algorithms
# Easy (34.88%)
# Total Accepted:    32.9K
# Total Submissions: 94.4K
# Testcase Example:  '3\n2'
#
# There is a fence with n posts, each post can be painted with one of the k
# colors.
#
# You have to paint all the posts such that no more than two adjacent fence
# posts have the same color.
#
# Return the total number of ways you can paint the fence.
#
# Note:
# n and k are non-negative integers.
#
# Example:
#
#
# Input: n = 3, k = 2
# Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways
# are:
#
# post1  post2  post3
# ⁠-----      -----  -----  -----
# ⁠  1         c1     c1     c2
# 2         c1     c2     c1
# 3         c1     c2     c2
# 4         c2     c1     c1
# ⁠  5         c2     c1     c2
# 6         c2     c2     c1
#
#
#


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [k, k*k, 0]
        if n <= 2:
            if n == 0:
                return 0
            else:
                return dp[n-1]
        for i in xrange(2, n):
            dp[2] = (k-1)*(dp[0]+dp[1])
            dp[0], dp[1] = dp[1], dp[2]
        return dp[2]
