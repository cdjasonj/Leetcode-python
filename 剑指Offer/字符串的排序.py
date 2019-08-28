"""

输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。


主要是利用深度优先遍历，
"""


class Solution:
    def Permutation(self, ss):
        # write code here

        temp_perm = []
        permuations = []
        other_chars = [char for char in ss] # 还没有使用的字符
        if ss:
            return self._permutation(ss,other_chars,temp_perm,permuations)
        else:
            return permuations

    def _permutation(self,ss,other_chars,temp_perm,permuations):

        if len(temp_perm) == ss:

            permuations.append(temp_perm)
            print(temp_perm)

        else:

            temp_perm.append(other_chars.pop())
            self._permutation(ss,other_chars,temp_perm,permuations)
            #回溯
            temp_perm.pop()


s = Solution()
print(s.Permutation('abc'))