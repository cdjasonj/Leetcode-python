#输入一个递增排序的数组和一个数字S，在数组中查找两个数，
# 使得他们的和正好是S，
# 如果有多对数字的和等于S，输出两个数的乘积最小的。


#因为是排序的，两头夹就可以了
# def FindNumbersWithSum(array,num):
#     result = []
#     left = 0
#     right = len(array) - 1
#
#     while left < right:
#
#         if array[left] + array[right] == num:
#             result.append((array[left],array[right]))
#             right -= 1
#         elif array[left] + array[right] > num:
#             right -= 1
#         else:
#             left+=1
#
#     min = result[1][0] * result[1][1]
#     temp = result[1]
#     for _result in result:
#         if _result[0]*_result[1] < min:
#             temp = _result
#
#     return temp[0],temp[1]


"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        left, right = 0,len(array) - 1
        Sums = []
        while left <= right:
            if array[left] + array[right] == tsum:
                Sums.append((array[left],array[right]))
                left += 1
            elif array[left] + array[right] < tsum:
                left += 1
            elif array[left] + array[right] > tsum:
                right -= 1

        if len(Sums) == 0 :
            return Sums

        else: return self._findMaxNum(Sums)

    def _findMaxNum(self,Sums):
        min = float('-inf')
        num1,num2 = None,None

        for _num1,_num2 in Sums:

            if _num1*_num2 < min:
                min = _num1 * _num2
                num1,num2 = _num1,_num2

        return num1,num2



#
# if __name__ == '__main__':
#
#     list = [1,1,2,3,3,3,4,5,6,7,8,9,22,24,25]
#     num = 29
#
#     print(FindNumbersWithSum(list,num))