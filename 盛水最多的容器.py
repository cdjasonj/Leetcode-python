

"""
#1, 暴力解 时间复杂度 oo(n^2)
ACE 不了
"""
# class Solution:
#     def maxArea(self, height):
#         if not height:
#             return 0
#         max_num = 0
#         for i in range(len(height)):
#             for j in range(i+1,len(height)):
#                 weight = j - i
#                 height1 = height[i]
#                 height2 = height[j]
#                 _height = min(height1,height2)
#
#                 if _height * weight > max_num:
#                     max_num = _height * weight
#         return max_num

"""
解法2 ，双指针向中间移动
移动双指针可能存在的情况:   
1,移动长板部分，不变，或者减小
2，移动短板部分，不变，减小，增大。

所有双指针移动策略， 移动短板

"""
class Solution:
    def maxArea(self, height):
        if not height:
            return 0
        left,right = 0,len(height)-1
        max_num = 0
        while left < right:
            weight = right - left
            min_height = min(height[left],height[right])
            if max_num < weight * min_height:
                max_num = weight * min_height

            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_num

S = Solution()
print(S.maxArea( [1,8,6,2,5,4,8,3,7]))