#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
#
# Easy (46.31%)
# Total Accepted:    141240
# Total Submissions: 303715
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times). However, you may not engage in multiple transactions at the
# same time (ie, you must sell the stock before you buy again).
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 :
            return 0
        TotalProfit = 0
        for i in range(1,len(prices)):
            if prices[i]> prices[i-1]:
                TotalProfit = TotalProfit + prices[i]- prices[i-1]
        return TotalProfit
