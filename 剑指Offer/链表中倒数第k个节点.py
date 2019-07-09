from tools import LinkList

def FindKthToTail(head,k):
    p = head.next
    q = head.next
    num = 1
    while p and num != k:
        p = p.next
        num+=1
    while p.next : #遍历到最后一个之前
        p = p.next
        q = q.next
    return q

if __name__ == '__main__':
    link_data = [2,4,5,1,2,22,4]
    print(link_data)
    LinkNode = LinkList.Create_LinkList(link_data)
    q = FindKthToTail(LinkNode,3)
    LinkList.Print_LinkList(q)