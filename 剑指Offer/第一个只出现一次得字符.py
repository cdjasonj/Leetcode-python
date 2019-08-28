#在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
# 并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
#ord()

#
#利用asci II 作为哈希，存储出现得次数，
#然后遍历元数组，找出哈希表中次数为1得，
def FirstNotRepeatingChar(s):
    hash = [0] * 256
    for _str in s:
        hash[ord(_str)] += 1

    for index,_str in enumerate(s):
        if hash[ord(_str)] == 1:
            return index
    return -1

if __name__ == '__main__':
    print(FirstNotRepeatingChar('sssad,asdadqwrqvxzcaff'))