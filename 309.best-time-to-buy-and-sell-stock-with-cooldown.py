#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (42.19%)
# Total Accepted:    63.5K
# Total Submissions: 150.3K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
#
#
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
#
#
# Example:
#
#
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#
#
#


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        buy,  sell, preSell = -prices[0], 0, 0
        for i in xrange(1, n):
            tmp = sell
            sell = max(sell, buy+prices[i])
            buy = max(preSell-prices[i], buy)
            preSell = tmp
        return sell
