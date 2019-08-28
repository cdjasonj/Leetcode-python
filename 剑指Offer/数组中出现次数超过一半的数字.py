#数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

def MoreThanHalfNum_Solution(numbers):
    #方法1 ，用字典， 时间复杂度on
    dic = {}
    for num in numbers:
        dic[num] = dic.get(num,0) +1

    for num,counts in dic.items():
        if counts >= len(numbers) //2 :
            return num

if __name__ ==  '__main__':
    list = [1,2,3,2,2,2,5,4,2]
    print(MoreThanHalfNum_Solution(list))