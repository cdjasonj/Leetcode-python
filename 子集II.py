#列表中含有重复数字，
#但是子集不能重复， 也就是说，在同一层不能使用同样的数字。

class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        #先将数组排序，
        nums.sort()
        n = len(nums)
        result = []

        def bt(i,temp):
            result.append(temp)

            for j in range(i,n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                else:
                    bt(j+1,temp + [nums[j]])

        bt[0,[]]

        return result