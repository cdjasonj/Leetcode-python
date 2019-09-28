class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # dp(i) = min(dp[i-2] + arr[i-2] , dp[i-1] + arr[i-1])
        # dp[0],dp[1] = 0,0
        # 他求得是跳完整个阶梯得花费， 也就是 数组后得一个数，
        #min(dp[-1] + cost[-1], dp[-2] + cost[-2])

        if not cost:
            return 0

        dp = [0] * len(cost)  # 初始化动态规划状态

        for idx in range(2, len(cost)):
            A = dp[idx - 2] + cost[idx - 2]
            B = dp[idx - 1] + cost[idx - 1]

            dp[idx] = min(A, B)

        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])
