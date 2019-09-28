class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # 动态规划， dp[i] 为，第i个数字，能贡献几个等差数组，
        # if A[i] - A[i-1] = A[i-1] - A[i-2] dp[i] = dp[i-1] + 1
        # 初始化， 考虑 考虑前三是否能构成等差数组

        if len(A) < 3:
            return 0
        dp = [0] * len(A)

        if A[1] - A[0] == A[2] - A[1]:
            dp[2] = 1

        for idx in range(3, len(A)):

            if A[idx] - A[idx - 1] == A[idx - 1] - A[idx - 2]:
                dp[idx] = dp[idx - 1] + 1

        return sum(dp)