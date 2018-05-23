#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges/description/
#
# algorithms
# Medium (23.08%)
# Total Accepted:    39.7K
# Total Submissions: 172K
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
# Given a sorted integer array nums, where the range of elements are in the
# inclusive range [lower, upper], return its missing ranges.
#
# Example:
#
#
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
#
#
#


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            return [str(lower)] if lower == upper else [str(lower)+"->"+str(upper)]
        ret = []
        if nums[0] > lower:
            if nums[0] == lower+1:
                ret.append(str(lower))
            else:
                ret.append(str(lower)+"->"+str(nums[0]-1))
        for a, b in zip(nums, nums[1:]):
            l = a+1
            u = b-1
            if l > u:
                continue
            if l == u:
                ret.append(str(u))
            else:
                ret.append(str(l)+"->"+str(u))
        if nums[-1] < upper:
            if nums[-1] == upper-1:
                ret.append(str(upper))
            else:
                ret.append(str(nums[-1]+1)+"->"+str(upper))
        return ret
