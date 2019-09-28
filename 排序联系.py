#简单插入排序

def inserOrder(list_node):

    for i in range(1,len(list_node)):

        j = i -1  #有序区第一个元素
        temp = list_node[i]

        while j >=0  and temp < list_node[j]:
            list_node[j+1] = list_node[j]
            j -= 1

        list_node[j+1] = temp
    return list_node


#希尔排序
#等距离的简单插入排序

def shellOrder(list_node):
    d = len(list_node) // 2

    while d:
        for i in range(d,len(list_node),d):
            j = i-d
            temp = list_node[i]
            while j >= 0 and temp < list_node[j]:
                list_node[j+d] = list_node[j]
                j -= d
            list_node[j+d] = temp
        d = d // 2
    return list_node
#简单选择排序
def selectOrder(list_node):

    #最后一个元素自然有序
    for i in range(0,len(list_node)-1):
        k = i
        for j in range(i,len(list_node)):
            if list_node[j] < list_node[k]:
                k  = j
        if k != i :
            temp = list_node[i]
            list_node[i] = list_node[k]
            list_node[k] = temp
    return list_node

#堆排序

#冒泡排序

def BubbleOrder(list_node):

    for i in range(0,len(list_node)):
        exchange = 0
        j = len(list_node) - 1

        while j != i :
            if list_node[j-1] > list_node[j]:
                temp = list_node[j-1]
                list_node[j-1] = list_node[j]
                list_node[j] = temp
                exchange = 1
            j -= 1
        if exchange == 0:
            break
    return list_node

#快速排序

def Quick_Sort(list_node,start,end):

    if start >= end:
        return

    left = start
    right = end
    temp = list_node[start]


    while left != right:
        while left < right and list_node[right] >= temp: #注意这个等于符号
            right -= 1
        list_node[left] = list_node[right]

        while left < right and list_node[left] <= temp:
            left +=1
        list_node[right] = list_node[left]

    list_node[left] = temp
    Quick_Sort(list_node,start,left-1)
    Quick_Sort(list_node,left+1,end)

    return list_node

#二分查找

if __name__ == '__main__':
    a = [46,46,79,56,39,40,84]
    # print(inserOrder(list_node))
    # print(shellOrder(list_node))
    # print(selectOrder(list_node))
    # print(BubbleOrder(list_node)
    print(Quick_Sort(a,0,len(a)-1))
