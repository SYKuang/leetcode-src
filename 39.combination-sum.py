#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum
#
# Medium (37.26%)
# Total Accepted:    155159
# Total Submissions: 412122
# Testcase Example:  '[2,3,6,7]\n7'
#
#
# Given a set of candidate numbers (C) (without duplicates) and a target number
# (T), find all unique combinations in C where the candidate numbers sums to
# T.
#
#
# The same repeated number may be chosen from C unlimited number of times.
#
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
#
#
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
#
# [
# ⁠ [7],
# ⁠ [2, 2, 3]
# ]
#
#
#


class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if len(candidates) == 0:
            return []
        for i in xrange(len(candidates) - 1, -1, -1):
            if candidates[i] == target:
                ret.append([target])
            elif candidates[i] < target:
                res = self.combinationSum(
                    candidates[:i + 1], target - candidates[i])
                # print len(res)
                for r in res:
                    r.append(candidates[i])
                ret = ret + res
        return ret
