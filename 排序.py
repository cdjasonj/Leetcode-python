
def insert_sort(list_node):
    #时间复杂度 on2 , 空间复杂度o1, 最好的情况下 时间复杂度on
    for index,data in enumerate(list_node):
        temp = data
        i = index - 1
        while i >=0  and temp < list_node[i]:
            list_node[i+1] = list_node[i]
            i -= 1
        list_node[i+1] = temp

def shell_sort(list_node):
    #希尔排序，时间复杂度不定
    # 等间隔的直接插入排序，每次执行完插入排序之后间隔为原来的一半，
    d = len(list_node)//2
    while d:
        for index in range(d,len(list_node),d):
            temp = list_node[index]
            i = index - d
            while i >= 0 and temp < list_node[i]:
                list_node[i+d] = list_node[i]
                i -= d
            list_node[i+d] = temp
        d = d//2

def selection_sort(list_node):
    #简单选择排序， 每次从未排序区选择最小的放在最前面
    #时间复杂度最好最坏都是ON2
    #简单选择排序，每次执行产生一个数全局有序
    for i in range(0,len(list_node),1):
        k = i
        for j in range(i+1,len(list_node),1):
            if list_node[j] < list_node[k] :
                k = j
        if k != i:
            temp = list_node[i]
            list_node[i] = list_node[k]
            list_node[k] = temp


def Sift(list_node,low,high):
    i = low
    j = low*2
    temp = list_node[i]
    while(j<=high):
        if j < high and list_node[j] < list_node[j+1]:
            j += 1
        if temp < list_node[j]:
            list_node[i] = list_node[j]
            i = j
            j = j*2
        else:
            break
    list_node[i] = temp

def Heap_Sort(list_node):
    # 堆排序， 思想，每次将堆结构中的最后一个和第一个交换位置。
    # 时间复杂度， 最好最坏，平均都是 nlog2n
    i = len(list_node)//2 #最后一个夫节点
    while i >= 0 :
        Sift(list_node,i,len(list_node)-1)
        i -= 1

    i = len(list_node)-1

    while i >= 0:
        temp = list_node[0]
        list_node[0] = list_node[i]
        list_node[i] = temp
        Sift(list_node,0,i-1)
        i -= 1
#
# def BubbleSort(list_node):
#     #时间复杂度 平均On2, 最坏On2, 最好On
#     #结束条件，一次遍历没有发生交换，代表着全局有序。
#     i = 0
#     while i < len(list_node):
#         exchange = 0
#         j = len(list_node) - 1
#
#         while j > i :
#             if list_node[j] < list_node[j-1]:
#                 temp = list_node[j]
#                 list_node[j] = list_node[j-1]
#                 list_node[j-1] = temp
#                 exchange = 1
#             j -= 1
#         if exchange == 0:
#             break
#         else:
#             i += 1


#冒泡排序:

def BubbleSort(list_node):

    for i in range(0,len(list_node)):
        flag =0

        j= len(list_node) - 1
        while j > i:
            if list_node[j] < list_node[j-1]:
                temp = list_node[j]
                list_node[j] = list_node[j-1]
                list_node[j-1] = temp
                flag = 1
            j -= 1
        if flag == 0:
            break

def Quick_Sort(list_node,start,end):

    if start >= end:
        return

    left = start
    right = end
    temp = list_node[start]


    while left != right:
        while left < right and list_node[right] > temp: #注意这个等于符号
            right -= 1
        list_node[left] = list_node[right]

        while left < right and list_node[left] < temp:
            left +=1
        list_node[right] = list_node[left]

    list_node[left] = temp
    Quick_Sort(list_node,start,left-1)
    Quick_Sort(list_node,left+1,end)


# def Merge_Sort(list_node):
#     埋坑

if __name__ == '__main__':
    a = [46,79,56,39,40,84]
    # insert_sort(a)
    # shell_sort(a)
    #selection_sort(a)
    # Heap_Sort(a)
    # BubbleSort(a)
    Quick_Sort(a,0,len(a)-1)
    #归并排序埋坑
    print(a)