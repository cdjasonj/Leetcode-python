"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。


输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

思路动态规划：

dp[i] 表示第i个节点与哪些开始节点节点可以构成回文串
列dp[i] = [2,4,5]
状态转移： dp[i+1] : 如果arr[i+1] = (2,4,5) - 1， 则 ，他就可以构成一个回文子串得开始,
初始化dp []
"""
class Solution:
    def countSubstrings(self, s):
        if not s:
            return 0
        dp = [[i] for i in range(len(s))]
        result = len(s)
        for i in range(1,len(s)):
            for j in dp[i-1]:
                #j == i-1时要进行两次判断，
                if j == i-1 :
                    if s[j] == s[i]:
                        dp[i].append(j)
                        result+=1
                if j-1 >= 0 and s[j-1] == s[i]:
                    dp[i].append(j-1)
                    result+=1
        return result

S = Solution()
print(S.countSubstrings('aaa'))