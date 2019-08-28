"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
my solution 
直接用str解决了。。。
时间on(来自比较) 空间On
"""


"""
其他思路。
数字解法，每次比较-1,1 .-2 ,2 的数字是否匹配。
o(n) o(1)
"""


#注意python 里的 // 和 /

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # 将这个数重排一下，判断是否和重排前相等.
        y, s = 0, 0  # y保存重排之后的数，s 保存余数

        # 当x < 0 时肯定时错的
        if x < 0:
            return False

        s = x

        while s != 0:
            y = y * 10 + s % 10
            s = s // 10

        if y != x:
            return False
        else:
            return True


Solution().isPalindrome(121)