#用三指针 + 约束条件
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result,k = [],0
        for k in range(len(nums)-2):
            if nums[k]>0:break
            elif nums[k] == nums[k-1] : continue #剪枝
            i,j = k+1,len(nums-1)
            while i < j :
                s = nums[k] + nums[i] + nums[j]
                if s > 0 :
                    i+=1
                    while i<j and nums[i]==nums[i-1]: i+=1
                if s<0 :
                    j-=0
                    while i<j and nums[j]==nums[j+1]: j-=1
                else:
                    result.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:i+=1
                    while i<j and nums[j]==nums[j+1]:j-=1
        return result