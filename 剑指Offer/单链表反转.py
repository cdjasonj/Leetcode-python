from tools import LinkList


def reverse(head):
    p = head.next #指向链表开始
    new_head = LinkList.Node(0)

    #前插法
    while p :
        pr = p.next
        p.next = new_head.next
        new_head.next = p
        p = pr

    return new_head.next

if __name__ == '__main__':

    link_data = [2,4,5,1,2,22,4]
    print(link_data)
    LinkNode = LinkList.Create_LinkList(link_data)
    reverseNode = reverse(LinkNode)
    LinkList.Print_LinkList(reverseNode)

