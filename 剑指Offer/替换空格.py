def replaceSpace(s):
    #将字符串中每一个空格替换成  %20 .
    new_string = ''
    for char in s:
        if char != ' ':
            new_string+=char
        else:
            new_string += '%20'
    return new_string

if __name__ == '__main__':
    print(replaceSpace('We Are Happy'))
