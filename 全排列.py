#给定一个没有重复数字的序列，返回其所有可能的全排列。
"""
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def permute(self,nums):

        def backtrack(first =0 ):
            #如果全部数字被用上。
            if first == n :
                output.append(nums[:])
            for i in range(first,n):
                #将第i个数放在最前面。
                nums[first],nums[i] = nums[i],nums[first]
                backtrack(first + 1)
                #backtrack
                nums[first],nums[i] = nums[i],nums[first]

        n = len(nums)
        output = []
        backtrack()

        return output

P = Solution()
print(P.permute([1,2,3]))