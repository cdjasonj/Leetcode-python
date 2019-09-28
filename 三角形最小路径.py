class Solution:
    def minimumTotal(self, triangle):

        if not triangle:
            return 0
        depth = len(triangle)
        widths = [len(_list)  for _list in triangle]
        dp = [[0]*len(arr) for arr in triangle]
        dp[0][0] = triangle[0][0]

        for m in range(1,depth):
            for n in range(widths[m]):
                # 分成三种情况，n为中间得元素，左边得元素，右边的元素
                if n == 0:
                    dp[m][n] = dp[m-1][n] + triangle[m][n]
                elif n == widths[m]-1: #最右边得元素
                    dp[m][n] = dp[m-1][n-1] + triangle[m][n]
                else:
                    A = dp[m-1][n-1] +triangle[m][n]
                    B = dp[m-1][n] + triangle[m][n]
                    dp[m][n] = min(A,B)                # if n-1>0:
        return min(dp[-1])

a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

S = Solution()
print(S.minimumTotal(a))
