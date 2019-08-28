
#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。
def reOrderArray(array):
    new_array_1 = []
    new_array_2 = []
    for item in array:
        if item%2 == 0:
            new_array_1.append(item)
        else:
            new_array_2.append(item)
    
    return new_array_1+new_array_2

if __name__ == '__main__':
    list_data1 = [2, 3, 4, 5, 5, 6, 6, 662, 200]
    array = reOrderArray(list_data1)
    print(array)