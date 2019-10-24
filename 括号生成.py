"""
本质上是一个回溯
在解空间的每个节点有两种选择，
1，添加左括号
2，添加右括号

为了保证添加括号的有效性，在遍历解空间的时候
1的条件: 左边括号剩余数>0
2的条件：只有在左边括号剩余小于右边括号剩余的时候再添加

返回结果条件。 left = right = 0
"""


class Solution:
    def generateParenthesis(self, n):

        if n == 0:
            return []
        result = []

        def backtrack(temp,left,right):
            if left == right and left == 0:
                result.append(temp)
            if left > 0:
                backtrack(temp+'(',left-1,right)
            if left < right:
                backtrack(temp+')',left,right-1)

        backtrack('',n,n)

        return result
S = Solution()
print(S.generateParenthesis(3))