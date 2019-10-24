
"""

暴力， o(n*k) java能过 python 过不了
"""
# class Solution:
#     def rotate(self, nums, k) :
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             last_num = nums[-1]
#             for j in range(len(nums)):
#                 temp = nums[j]
#                 nums[j] = last_num
#                 last_num = temp


S = Solution()
S.rotate([1,2,3,4,5,6,7],3)