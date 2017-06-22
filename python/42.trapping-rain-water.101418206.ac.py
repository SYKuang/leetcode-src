#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water
#
# Hard (36.10%)
# Total Accepted:    111163
# Total Submissions: 306479
# Testcase Example:  '[]'
#
# 
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after
# raining. 
# 
# 
# 
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# 
# 
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = -1
        right = -1
        bLeft = False
        Water = 0
        ground = 0
        
        for i in range(len(height)):
            if height[i] > 0:
                    left = i
                    ground = height[i]
                    bLeft = True
                    break
           
        while left < len(height) and bLeft:
            j = left + 1
            bRight = False
            if left < len(height)-1 and height[left] > height[left+1]:
                maxRight = -1
                while j < len(height):
                    if maxRight == -1 or height[maxRight] <= height[j]:
                        maxRight = j
                    
                    if height[j] >= height[left]:
                        right= j
                        bRight = True
                        break
                    else:
                        j = j+1
                    
                if bRight == False:
                    right = maxRight
                #print left,right
                for i in range(left+1,right):
                    if min(height[left],height[right]) - height[i] > 0:
                        Water = Water + min(height[left],height[right]) - height[i]
                    #print left,right
                left = right
            
            else:
                left = left + 1
        return Water
