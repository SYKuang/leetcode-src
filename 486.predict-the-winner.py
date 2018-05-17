#
# [486] Predict the Winner
#
# https://leetcode.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (45.26%)
# Total Accepted:    26.9K
# Total Submissions: 59.5K
# Testcase Example:  '[1,5,2]'
#
# Given an array of scores that are non-negative integers. Player 1 picks one
# of the numbers from either end of the array followed by the player 2 and then
# player 1 and so on. Each time a player picks a number, that number will not
# be available for the next player. This continues until all the scores have
# been chosen. The player with the maximum score wins.
#
# Given an array of scores, predict whether player 1 is the winner. You can
# assume each player plays to maximize his score.
#
# Example 1:
#
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. If he chooses 2
# (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5,
# then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 +
# 2 = 3, and player 2 is 5. Hence, player 1 will never be the winner and you
# need to return False.
#
#
#
# Example 2:
#
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5
# and 7. No matter which number player 2 choose, player 1 can choose
# 233.Finally, player 1 has more score (234) than player 2 (12), so you need to
# return True representing player1 can win.
#
#
#
# Note:
#
# 1
# Any scores in the given array are non-negative integers and will not exceed
# 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.
#
#
#


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.table={}
        a1, b1 = self.helper(nums)
        if a1 >= b1:
            return True
        return False

    def helper(self, nums):

        if len(nums) < 3:
            return (max(nums), min(nums))
        t=tuple(nums)
        if t in self.table:
            return self.table[t]
        if len(nums) == 3:
            if nums[0]+min(nums[1:]) >= nums[-1]+min(nums[:-1]):
                return nums[0]+min(nums[1:]), max(nums[1:])
            else:
                return nums[-1]+min(nums[:-1]), max(nums[:-1])
        b1, a1 = self.helper(nums[1:])
        b2, a2 = self.helper(nums[:-1])
        if nums[0]+a1 >= nums[-1]+a2:
            self.table[t]=(nums[0]+a1, b1)

            return (nums[0]+a1, b1)
        else:
            self.table[t]=(nums[-1]+a2, b2)
            return (nums[-1]+a2, b2)
