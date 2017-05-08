#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water
#
# Medium (36.30%)
# Total Accepted:    131321
# Total Submissions: 361282
# Testcase Example:  '[1,1]'
#
# Given n non-negative integers a1, a2, ..., an, where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lh = 0
        rh = len(height)-1
        ans = min(height[lh],height[rh])*(len(height)-1)
        i = 0
        j = rh
        while i < j :
            tmp = min(height[lh],height[rh])*(rh-lh)
            #print ans
            #print "lh=" + str(lh) + "rh= " + str(rh)
            if ans < tmp:
                ans = tmp
            if height[lh] < height[rh]:
                while i <= j and height[i] <= height[lh]:
                    i=i+1
                if i < j:
                    lh=i
                    #print "lh=" + str(lh) + "rh= " + str(rh)
            else:
                while i<=j and height[rh] >= height[j]:
                    j=j-1
                #print "i=" + str(i) + " j=" + str(j)
            
                if i < j:
                    
                    rh=j
                    #print "lh=" + str(lh) + "rh= " + str(rh)
        return ans
