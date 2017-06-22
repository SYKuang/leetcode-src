#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest
#
# Medium (30.79%)
# Total Accepted:    126360
# Total Submissions: 409288
# Testcase Example:  '[0,0,0]\n1'
#
# Given an array S of n integers, find three integers in S such that the sum is
# closest to a given number, target. Return the sum of the three integers. You
# may assume that each input would have exactly one solution.
# 
# 
# ⁠   For example, given array S = {-1 2 1 -4}, and target = 1.
# 
# ⁠   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans=None
        nums=sorted(nums)
        
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l <r:
                tmp = nums[i] + nums[l] + nums[r]
                #print "i=%d l=%d r=%d" % (i,l,r) 
                if ans is None or abs(tmp -target) < abs (ans - target):
                    ans = tmp
                if tmp > target:
                    r =r-1
                else:
                    l = l+1

        return ans

