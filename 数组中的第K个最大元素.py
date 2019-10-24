"""
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
"""

"""
方法1 ， 用冒泡排序， 从左边开始冒出最大的，执行N次
#时间复杂度会超

方法2： 一直执行快排，每一趟快排返回该次到位的数据的下标，知道返回的下标为k

"""


class Solution:
    def findKthLargest(self, nums,k):
        def fastSort(start,end):
            left = start
            right = end
            temp = nums[start]
            while left != right:
                while left < right and nums[right] > temp:  # 注意这个等于符号
                    right -= 1
                nums[left] = nums[right]

                while left < right and nums[left] < temp:
                    left += 1
                nums[right] = nums[left]

            nums[left] = temp
            return left
        
        print(fastSort(0,len(nums)-1))
S = Solution()
print(S.findKthLargest( [3,2,1,5,6,4],2))