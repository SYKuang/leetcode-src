#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii
#
# Medium (32.19%)
# Total Accepted:    117706
# Total Submissions: 365556
# Testcase Example:  '[1,1,2]'
#
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
#
#
#
# For example,
# [1,1,2] have the following unique permutations:
#
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#
#


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []
        self.visited = [False for _ in xrange(len(nums))]
        cur = []
        self.permuteRes(sorted(nums),  cur)
        return self.ret

    def permuteRes(self, nums,  curr):
        if len(curr) == len(nums):
            self.ret.append(list(curr))
        else:
            for i in xrange(len(nums)):
                if self.visited[i] or (i > 0 and nums[i - 1] == nums[i] and not self.visited[i - 1]):
                    continue
                self.visited[i] = True
                curr.append(nums[i])
                self.permuteRes(nums,  curr)
                curr.pop()
                self.visited[i] = False
