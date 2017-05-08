#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum
#
# Medium (21.48%)
# Total Accepted:    211017
# Total Submissions: 980728
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array S of n integers, are there elements a, b, c in S such that a +
# b + c = 0? Find all unique triplets in the array which gives the sum of
# zero.
# 
# Note: The solution set must not contain duplicate triplets.
# 
# 
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#
class Solution(object):
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
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        snums=sorted(nums)


        for i in range(0,len(snums)-2):
            if i > 0 and snums[i]==snums[i-1]:
                continue

            tmp=self.twoSum(snums,0,i)
            for numset in tmp:
                ans.append(numset)
        return ans
        

