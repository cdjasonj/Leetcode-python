"""
动态规划
1,2,3,4,5,6
a,b,a,c,b,b
dp[i] = list[]
dp[i]中的元素记录了，以i为结束， 最长的子串的下标
比如dp[3] = [2,3]
dp[4] = [2,3,4]
dp[5] = [3,4,5]

递推公式

dp[i+1] for idx in dp[i+1] if arr[idx] == arr[i+1] => dp[i+1] = arr[idx+1:i+1]

初始化， dp[1] = 1

保存每个动态规划数组长度， 返回最大值
"""


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         dp = [[] for char in s]
#         dp[0].append(0)
#         max_len = 1
#         for i in range(1,len(s)):
#             flag = 0
#             for idx,j in enumerate(dp[i-1]):
#                 if s[j] == s[i]:
#                     dp[i].extend(dp[i-1][idx+1:])
#                     dp[i].append(i)
#                     if len(dp[i]) > max_len:
#                         max_len = len(dp[i])
#                     flag = 1
#                     break
#             if flag == 0: #
#                 dp[i].extend(dp[i-1])
#                 dp[i].append(i)
#                 if len(dp[i]) > max_len:
#                     max_len = len(dp[i])
#         return max_len

#利用set 的 remove 和add 实现滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return None
        left = 0
        lookup = set()
        maxlen = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len +=1
            while s[i] in lookup:
                lookup.remove(s[left])
                left +=1
                cur_len -= 1
            if cur_len > maxlen:
                maxlen = cur_len
            lookup.add(s[i])

        return maxlen



S = Solution()
print(S.lengthOfLongestSubstring('bbtablud'))