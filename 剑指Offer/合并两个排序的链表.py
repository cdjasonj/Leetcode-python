from tools import LinkList

#输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

def merge(head1,head2):
    new_head = LinkList.Node(0)
    p = head1.next
    q = head2.next
    k = new_head

    while p and q:
        if p.val <= q.val:
            k.next = p
            p = p.next
            k = k.next
        else:
            k.next = q
            q = q.next
            k = k.next

    while p :
        k.next = p
        p = p.next
        k = k.next

    while q :
        k.next = q
        q = q.next
        k = k.next
    return new_head

if __name__ =='__main__':

    list_data1 =  [2,3,4,5,5,62,200]
    list_data2 = [5,10,23,224,335]
    HeadNode1 = LinkList.Create_LinkList(list_data1)
    HeadNode2 = LinkList.Create_LinkList(list_data2)
    new_head = merge(HeadNode1,HeadNode2)
    LinkList.Print_LinkList(new_head)