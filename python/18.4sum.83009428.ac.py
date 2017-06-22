#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum
#
# Medium (26.26%)
# Total Accepted:    115637
# Total Submissions: 438179
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
# 
# Note: The solution set must not contain duplicate quadruplets.
# 
# 
# 
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        nums=sorted(nums)
        for i in range(0,len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            tmp=self.threeSum(nums,target,i)
            for numset in tmp:
                ans.append(numset)
        return ans

    def twoSum(self,nums,target,idx):
        i=idx+1
        j=len(nums)-1
        ans=[]

        while i<j:
            #print "i="+str(i)+ " j="+str(j)
            
            
            tmp=nums[i] + nums[j] + nums[idx]

            if  tmp == target:
                if len(ans)==0 or ans[len(ans)-1] != tmp:
                    ans.append([nums[idx],nums[i],nums[j]])
                i=i+1
                j=j-1
                while i < j and nums[j]==nums[j+1]:
                    j=j-1
                while i<j and nums[i]==nums[i-1]:
                    i=i+1
            elif tmp > target:
                j=j-1
            else:

                i=i+1

        return ans
    def threeSum(self, nums,target,idx):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]

        for i in range(idx+1,len(nums)-2):
            if i!=idx+1 and nums[i] == nums[i-1]:
                continue

            
            tmp=self.twoSum(nums,target-nums[idx],i)
            for numset in tmp:
                tmpNumSet= numset
                tmpNumSet.insert(0,nums[idx])
         
                ans.append(tmpNumSet)

        return ans
        




