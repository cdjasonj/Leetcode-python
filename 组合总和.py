
#这个题很有味道，
#1，数组传入栈的写法，
#2，一个数字可以被反复使用的写法， 传入的是当前传入的下标， 而不是 i+1 。这样就可以实现反复调用
#3，排序 剪枝。
#4， 内部内实现递归
class Solution:
    def combinationSum(self, candidates,target):

        #排序用来剪枝
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i,temp_sum,temp):
            if temp_sum > target or i == n:
                return
            if temp_sum == target:
                res.append(temp)
            #
            for j in range(i,n):
                if temp_sum + candidates[j] > target:
                    break
                #传入j 而不是i +1 ,这样可以实现重复某个数字的使用
                backtrack(j,temp_sum+candidates[j],temp+[candidates[j]]) #这样写可以入栈
        backtrack(0, 0, [])
        return res
S = Solution()
print(S.combinationSum( [2,3,5],8))