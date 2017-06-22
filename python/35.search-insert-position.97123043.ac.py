#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position
#
# Easy (39.37%)
# Total Accepted:    171153
# Total Submissions: 433505
# Testcase Example:  '[1]\n0'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# 
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0
# 
#
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(end+start)/2
            
            if target < nums[mid]:
                end=mid-1
                if end >=0:
                    if target >nums[end]:
                        return end+1
                else:
                    return 0
            elif target > nums[mid]:
                start=mid+1
                if start < len(nums):
                    if target < nums[start]:
                        return start
                else:
                    return len(start)
            else:
                return mid
            
      
