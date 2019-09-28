"""
问题定义：
重量数组 w = {4,6,2,2,5,1}
价格数组 v = {8,10,6,3,7,2}
背包容量  C = 12
例：0-1背包问题。在使用动态规划算法求解0-1背包问题时，

动态规划：
1，子问题拆解 dp[i][j] 表示只有i个商品，背包重量为j的最大价值
2，状态转移 dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

"""
import numpy as np
def dp_knapack(weights,values,C):
    dp = np.zeros(shape=(len(weights),C))
    #初始化dp[1][1-n]
    dp[0][weights[0]-1:] = values[0]
    for i in range(1,len(weights)):
        for j in range(C):
            if weights[i] <= j:
                #状态转移方程
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[-1][-1]

"""
0-1背包问题， 回溯法解决：
1，定义解空间
2，定义约束条件
3，DFS，保存所有可能的答案
4，返回答案的最大值
"""


class Solution():
    def __init__(self):

        self.result = []

    def start(self,weights,values,C):

        self.knapack(weights,values,0,C)
        print(self.result)
        return max(self.result)

    #其实这里传到达的层次数 i 就可以了
    def knapack(self,weights,values,sum_value,C):
        """
        :param weights:
        :param values:
        :param C:  剩余的重量
        :return:
        """
        if not weights and not values: #到最后一个了。
            self.result.append(sum_value)
            return

        if weights[0] > C: #装不下了
            self.result.append(sum_value)
            return

        #case1 不装
        self.knapack(weights[1:],values[1:],sum_value,C)
        #case2 装
        sum_value = sum_value + values[0]
        C = C - weights[0]
        self.knapack(weights[1:],values[1:],sum_value,C)

S = Solution()
print(dp_knapack([4,6,2,2,5,1],[8,10,6,3,7,2],12))
# weights = [4,6,2,2,5,1]
# values = [8,10,6,3,7,2]
# print(S.start(weights,values,12))