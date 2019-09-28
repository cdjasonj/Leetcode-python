"""
1，需要考虑字符串中是否存在非括号字符
2，嵌套情况下匹配，括号嵌套，其最里面一层一定是相邻匹配的
3，遇到左括号入栈，遇到右括号，判单是否与
"""


class Solution:
    def isValid(self, s):
        if not s:
            return True
        left_sets = {'(':')','[':']','{':'}'}
        right_sets = {')':'(',']':'[','}':'{'}
        stack = []
        for char in s:
            if char in left_sets:
                stack.append(char)
            elif char in right_sets and stack:
                left = stack.pop()
                if left_sets[left] != char:
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False

S = Solution()
print(S.isValid('{[]}'))