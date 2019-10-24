"""

不同于之前的，这个版本要求可以多次买卖股票

思路， 如果第一个数字大于第二个数字， 遍历整个数组，  这个总和就是可以获得的总利润

完整的思路来自于 利润最大化，不能跳过任何一个峰值的逻辑

本质上也是一个贪心，
"""
class Solution:
    def maxProfit(self, prices) :
        total_profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
        return total_profit
