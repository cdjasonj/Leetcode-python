class Solution:
    def letterCombinations(self, digits):

        if digits:

            self.n = len(digits)
            self.alphs = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],
                     5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],
                     8:['t','u','v'],9:['w','x','y','z']}
            self.digits = digits
            self.result = []
            self.dfs(0,'')
            return self.result
        else:
            return None

    def dfs(self,i,str):

        if i == self.n : # 遍历到解空间树的叶子节点
            self.result.append(str)
            return

        for alp in self.alphs[int(self.digits[i])]:

            # str += alp #这样写答案不对。 这样写应该是字符串在地址持久化保存了，
            self.dfs(i+1,str+alp) #这样写才会进入系统栈

S = Solution()
print(S.letterCombinations('23'))