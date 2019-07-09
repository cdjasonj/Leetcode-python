from tools import LinkList


def printListFromTailToHead(HeadNode):
    #按栈输入输出就可以了
    stack = []
    revers_data = []
    p = HeadNode.next
    while p:
        stack.append(p.val)
        p = p.next
    for data in range(len(stack)):
        data = stack.pop()
        revers_data.append(data)
    return revers_data

if __name__ =='__main__':

    list_data=  [2,3,4,5,5,67,8,10]
    HeadNode = LinkList.Create_LinkList(list_data)
    revers_data = printListFromTailToHead(HeadNode)
    print(revers_data)