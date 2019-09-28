import numpy as np


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # 动态规划， 优化子问题 dp[i][j] = min(arr[i][j] + dp[i-1][j], arr[i][j] + dp[i][j-1])
        #矩阵的路径问题，主要要注意他得边界问题。

        m, n = len(grid), len(grid[0])
        if not grid:
            return 0
        if m == 1:
            return sum(grid[0])
        if n == 1:
            return sum([num[0] for num in grid])

        dp = np.zeros(shape=(m, n))
        dp[0][0], dp[1][0], dp[0][1] = grid[0][0], grid[0][0] + grid[1][0], grid[0][0] + grid[0][1]

        for i in range(m):
            for j in range(n):
                if (i == 1 and j == 0) or (i == 0 and j == 1):
                    continue
                elif i - 1 >= 0 and j - 1 >= 0:
                    A = dp[i - 1][j] + grid[i][j]
                    B = dp[i][j - 1] + grid[i][j]
                    dp[i][j] = min(A, B)
                elif i - 1 >= 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]

        return int(dp[m - 1][n - 1])

