#在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留
# ，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
from tools import LinkList
def deleteDuplication(pHead):
    p = pHead

    while p and p.next:
        if p.val == p.next.val:
            p = del_node(p)
        p = p.next

    return pHead

def del_node(head):
    temp = head
    while temp and temp.val == head.val:
        temp = temp.next
    head.next = temp
    return head


if __name__ =='__main__':

    list_data1 =  [2,3,4,5,5,6,6,662,200]
    HeadNode1 = LinkList.Create_LinkList(list_data1)
    new_head = deleteDuplication(HeadNode1)
    LinkList.Print_LinkList(new_head)