#把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。
#  习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


#规律， 丑数肯定是由一个 丑数乘 2，3，5 得来的。
# 要从小到大的顺序得到低N个丑数， 则 每次要在可能的丑数中选出最小的， 生成
#维护 三组数组， 一组是乘3的，一组是乘5的，一组是乘2的，每次从三组队列头部取出最小的
#然后将取出来的乘2，3，5，放到队列

import queue

# 方法1 ， 遍历所有数，判断这个数是否是丑数，  低效


# -*- coding:utf-8 -*-
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。
#  习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

# 规律， 丑数肯定是由一个 丑数乘 2，3，5 得来的。


# 方法1 ， 遍历所有数，判断这个数是否是丑数，  低效

# 牛客网通不过， 时间复杂度超了
# -*- coding:utf-8 -*-
# class Solution:
#     def GetUglyNumber_Solution(self, index):
#         # write code here
#
#         uglyNumbers = []
#
#         num = 1
#         while len(uglyNumbers) < index - 1:
#
#             if self._is_UglyNumber(num):
#                 uglyNumbers.append(num)
#
#             num += 1
#
#         return num
#
#     def _is_UglyNumber(self, num):
#
#         if num == 1:
#             return True
#
#         while num > 1:
#
#             if num%2== 0 :
#                 num = num/2
#
#             elif num % 3 == 0:
#                 num = num/3
#
#             elif num % 5 == 0 :
#                 num = num/5
#             else:
#                 return False
#
#         return True
#
#
# #方法2 每次找出 刚好大于 已经保存丑数的 下一个 2，3，5 倍数的丑数，让后从这三个 temp丑数中找出最小的那个丑数，最为下一次

class Solution:
    def GetUglyNumber_Solution(self, index):

        if index >= 1:
            uglyNumber = [1]

            for i in range(index):
                temp2, temp3, temp5 = 0, 0, 0
                for j in range(index):
                    temp2 = uglyNumber[j] * 2
                    if temp2 > uglyNumber[-1]:
                        break

                for j in range(index):
                    temp3 = uglyNumber[j] * 3
                    if temp3 > uglyNumber[-1]:
                        break

                for j in range(index):
                    temp5 = uglyNumber[j] * 5
                    if temp5 > uglyNumber[-1]:
                        break

                uglyNumber.append(min(temp2, temp3, temp5))

            return uglyNumber[index - 1]
        else:
            return 0