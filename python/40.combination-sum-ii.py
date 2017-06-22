#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii
#
# Medium (32.54%)
# Total Accepted:    112344
# Total Submissions: 341057
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
#
# Given a collection of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T.
#
#
# Each number in C may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
#
#
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
#
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
#


class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combinationSum(sorted(candidates), target)

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
                if [target] not in ret:
                    ret.append([target])
            elif candidates[i] < target:
                res = self.combinationSum(
                    candidates[:i], target - candidates[i])
                for r in res:
                    r.append(candidates[i])
                for r in res:
                    if r not in ret:
                        ret.append(r)
        return ret
