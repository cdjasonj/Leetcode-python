import numpy as np


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 动态规划问题， 第i天最大收益，等于max(dp(i-1),arr[i] - min )

        _min = prices[0]
        dp = [0] * (len(prices))  # 初始化n天最大收益

        for i in range(1, len(prices)):

            A = dp[i - 1]
            B = prices[i] - _min

            dp[i] = max([A, B])

            if _min > prices[i]:
                _min = prices[i]

        return dp[-1]

S = Solution()
print(S.maxProfit([7,1,5,3,6,4]))
