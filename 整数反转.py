# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# #
# # 示例 1:
# #
# # 输入: 123
# # 输出: 321
# #  示例 2:
# #
# # 输入: -123
# # 输出: -321
# # 示例 3:
# #
# # 输入: 120
# # 输出: 21
# # 注意:
# #
# # 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# #
# # 来源：力扣（LeetCode）
# # 链接：https://leetcode-cn.com/problems/reverse-integer
# # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#整数转负数不知道咋弄，用字符串解决的 时间复杂度 o(n)空间复杂度o(n)

class Solution:
    def reverse(self, x: int) -> int:
        temp = []
        a = 0
        flag = 0
        b = 1
        if x < 0:
            x = abs(x)
            flag = 1
        while x:
            temp.append(x % 10)
            x //= 10
        temp.reverse()
        for i in temp:
            a += b * i
            b *= 10
        if flag == 1:  # 原本位负数
            _str = '-' + str(a)
            a = int(_str)
        if a < -2 ** 31 or a > 2 ** 31 - 1:
            return 0
        else:
            return a

#别人的解决方法，用栈，我哪儿直接用reverse了，用栈的话会少reverse的执行时间
"""
执行用时 :
60 ms
, 在所有Python3提交中击败了
65.99%
的用户
内存消耗 :
13.1 MB
, 在所有Python3提交中击败了
92.96%
的用户"""
class Solution:
    def reverse(self, x: int) -> int:
        temp = []
        a = 0
        flag = 0
        b = 1
        if x < 0:
            x = abs(x)
            flag = 1
        while x:
            temp.append(x % 10)
            x //= 10

        while temp:
            i = temp.pop()
            a += b * i
            b *= 10
        if flag == 1:  # 原本位负数
            _str = '-' + str(a)
            a = int(_str)
        if a < -2 ** 31 or a > 2 ** 31 - 1:
            return 0
        else:
            return a

#还有另外一个思路，从头到尾都用字符串来执行，
class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 <= x < 0:
            x = str(x)[1:]
            x = x[::-1].lstrip('0')
            if int(x) > 2**31:
                return 0
            else:
                return int('-' + x)
        elif x == 0:
            return 0
        elif x < 2**31:
            x = str(x)[::-1].lstrip('0')
            if int(x) >= 2**31:
                return 0
            else:
                return int(x)