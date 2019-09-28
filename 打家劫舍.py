class Solution:
    def rob(self, nums: List[int]) -> int:

        #思路，动态规划
        #自顶向下，向前遍历 dp[i] 表示，遍历到底i步时候得最大值。
        #边界问题， dp[0] = arr[0], dp[1] = max(arr[0],arr[1])
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            A = dp[idx - 2] + nums[idx]
            B = dp[idx - 1]

            dp[idx] = max(A, B)

        return dp[-1]