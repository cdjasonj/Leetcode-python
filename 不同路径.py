import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 分解 dp[m][n] = d[m-1][n] + dp[m][n-1]
        # dp[m][n] 代表着到m,n得路径总数。
        if m == 1 or n == 1:
            return 1
        if m == 0 and n == 0:
            return 0
        dp = np.zeros(shape=(m,n))
        dp[0][0],dp[1][0],dp[0][1] = 0,1,1

        for i in range(0,m):
            for j in range(0,n):

                if (i ==1 and j == 0) or (i==0 and j==1):
                    continue
                else:
                    if j-1 >=0 and i-1 >=0 :
                        dp[i][j] = dp[i][j-1] + dp[i-1][j]
                    elif i-1 < 0:
                        dp[i][j] = dp[i][j-1]
                    elif j-1 < 0 :
                        dp[i][j] = dp[i-1][j]
        return int(dp[m-1][n-1])