#一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。




def FindNumsAppearOnce( array):

    dic = {}

    for num in array:
        dic[num] = dic.get(num, 0) + 1

    for num, count in dic.items():

        if count == 1:

            return num

if __name__ == '__main__':
    print(FindNumsAppearOnce([1,2,3,3,4,4,5,5,6,6]))
