# -*- coding:utf-8 -*-
"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

"""


def FirstNotRepeatingChar( s):
    # write code here

    dic = {}  #

    for index, char in enumerate(s):

        if char not in dic:
            dic[char] = (index, 1)
        else:
            index, count = dic.get(char)
            count += 1
            dic[char] = (index, count)

    for char, index_count in dic.items():
        if index_count[1] == 1:
            return index_count[0]


print(FirstNotRepeatingChar('NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp'))