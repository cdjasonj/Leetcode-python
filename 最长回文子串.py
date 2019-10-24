"""
用动态规划，
找出每个位置的所有回文串
状态转移与正常计算回文串数量的题相同
"""


class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ''
        dp = [[i] for i in range(len(s))]
        maxlen = 0
        maxlen_str = s[0]
        for i in range(1,len(s)):
            for j in dp[i - 1]:
                # j == i-1时要进行两次判断，
                # 当为两个字符的时候，判断两个字符是否相等
                if j == i - 1:
                    if s[j] == s[i]:
                        dp[i].append(j)
                if j - 1 >= 0 and s[j - 1] == s[i]:
                    dp[i].append(j - 1)

        for end_index in range(len(dp)):
            for start_index in dp[end_index]:
                cur_len = end_index - start_index
                if cur_len > maxlen:
                    maxlen = cur_len
                    maxlen_str = s[start_index:end_index+1]
        return maxlen_str

S = Solution()
print(S.longestPalindrome('cbbd'))
