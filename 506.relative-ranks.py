#
# [506] Relative Ranks
#
# https://leetcode.com/problems/relative-ranks/description/
#
# algorithms
# Easy (47.10%)
# Total Accepted:    31.1K
# Total Submissions: 66K
# Testcase Example:  '[5,4,3,2,1]'
#
#
# Given scores of N athletes, find their relative ranks and the people with the
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver
# Medal" and "Bronze Medal".
#
# Example 1:
#
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so
# they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two
# athletes, you just need to output their relative ranks according to their
# scores.
#
#
#
# Note:
#
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
#
#
#
#


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def getRanks(i):
            if i == 1:
                return "Gold Medal"
            elif i == 2:
                return "Silver Medal"
            elif i == 3:
                return "Bronze Medal"
            else:
                return str(i)
        q = []
        for i, n in enumerate(nums):
            heapq.heappush(q, (-n, i))
        res = [""]*len(nums)
        for order in xrange(len(nums)):
            _, i = heapq.heappop(q)
            res[i] = getRanks(order+1)
        return res
