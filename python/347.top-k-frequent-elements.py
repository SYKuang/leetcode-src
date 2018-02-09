#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (49.02%)
# Total Accepted:    86.3K
# Total Submissions: 176.1K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
#
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
#
#
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        table=dict()
        for i,v in enumerate(nums):
            if v in table:
                table[v]=table[v]+1
            else:
                table[v]=1
        table_x=sorted(table.items(), key=lambda x: x[1],reverse=True)
        ret=[]
        for i in xrange(k):
            ret.append(table_x[i][0])
        return ret
