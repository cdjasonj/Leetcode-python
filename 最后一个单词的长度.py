"""
输入: "Hello World"
输出: 5



直接遍历，维护一个当前遍历到的长度的变量
"""

class Solution:
    def lengthOfLastWord(self, s):
        length = 0
        for char in s:
            length += 1
            if char == ' ':
                length = 0
        return length
S = Solution()
print(S.lengthOfLastWord(" "))