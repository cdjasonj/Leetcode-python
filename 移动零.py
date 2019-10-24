"""
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        index1,index2 = 0,0 #双指针
        while index2 <= len(nums)-1 :

            if nums[index2] != 0 :
                #把index2放到合适的位置
                while index1 < index2 and nums[index1] !=0:
                    index1 += 1
                if index1 != index2:
                    temp = nums[index2]
                    nums[index2] = nums[index1]
                    nums[index1] = temp

            index2 += 1

S = Solution()
print(S.moveZeroes([1]))

