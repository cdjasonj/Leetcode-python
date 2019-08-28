"""

给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii

"""

#方法1 ， 用栈， 时间复杂度 o（n） o(n)

class Solution:
    def reverseWords(self, s: str) -> str:

        stack = []
        new_string = ''
        temp_string = ''
        for char in s:

            if char != ' ':
                stack.append(char)

            else:

                while stack:
                    temp_string += stack.pop()
                temp_string += ' '
                new_string += temp_string
                temp_string = ''

        while stack:
            temp_string += stack.pop()

        new_string += temp_string

        return new_string


#方法2 ，双向指针。
