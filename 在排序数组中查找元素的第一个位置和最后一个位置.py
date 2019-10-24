"""
基本思路就是用二分查找找出所有的，而不是在正常得二分查找，找出一个之后就停止
期间，用left,right变量记录最右和最左。
"""


class Solution:
    def searchRange(self, nums,target):

        def binarySearch(left,right,left_flag):

            while left <= right:
                mid = (left+right)//2
                if nums[mid] > target or (target == nums[mid] and left_flag):
                    #就算查找成功，也让查找在左区间继续
                    right = mid-1
                else:
                    left = mid+1
            return left

        left_index = binarySearch(0,len(nums)-1,True)
        #要判断一下 是否left_index 就是查找的数字
        if left_index == len(nums) or nums[left_index] != target:
            return [-1,-1]

        return [left_index, binarySearch(0, len(nums)-1, False)-1 ]

nums = [0,0,0,1,2,3]
target = 0
S = Solution()
print(S.searchRange(nums,target))