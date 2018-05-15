#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (37.82%)
# Total Accepted:    168.5K
# Total Submissions: 445.5K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        if l < 2:
            return 0
        ret = 0
        left=0
        right=l-1
        while left<right:
            h=min(height[left],height[right])
            if height[left]==h:
                left+=1
                while left<right and height[left]<h:
                    ret+=h-height[left]
                    left+=1
            else:
                right-=1
                while left<right and height[right]<h:
                    ret+=h-height[right]
                    right-=1

        return ret
