#在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留
# ，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


from tools import LinkList


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next and p.next.next:
            if p.next.val == p.next.next.val:
                self.del_node(p,p.next.val)
            p = p.next
        return head

    def del_node(self, head,val):
        # 找到第一个val != head.val
        temp = head.next
        while temp and temp.val == val:
            temp = temp.next
        head.next = temp

# write code here


if __name__ =='__main__':

    list_data1 =  [2,3,4,5,5,6,6,662,200]
    HeadNode1 = LinkList.Create_LinkList(list_data1)
    new_head = deleteDuplication(HeadNode1)
    LinkList.Print_LinkList(new_head)