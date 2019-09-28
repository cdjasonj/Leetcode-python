#其实就是保存每条路径的
#且解空间树，从上一个节点的下个数字开始，这样才不会出现重复

#类似于 组合总和
class Solution:
    def subsets(self, nums):

        if nums:
            n = len(nums)
            result = []

            def bt(i,temp):
                result.append(temp)
                for j in range(i,n):
                    bt(i+1,temp + [nums[j]])

            bt(0,[])
            return result
        else:
            return []