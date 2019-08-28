#用两个栈保存单链表，然后一一弹出，如果第一个不一样，那么他前一个就是公共链表.


# def FindFirstCommonNode(head1,head2):
#     p = head1.next
#     q = head2.next
#
#     stack1,stack2 = [],[]
#     while p:
#         stack1.append(p)
#         p = p.next
#     while q :
#         stack2.append(q)
#         q = q.next
#
#     pr = stack1[-1]
#     while stack1 and stack2:
#         if stack1.pop() != stack2.pop():
#             break
#         else:
#             pr = stack1.pop()
#             stack2.pop()
#
#     return pr


#输入两个链表，找出它们的第一个公共结点。

#遍历两个链表，将两个链表分别压入两个栈。然后同时出栈
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here

        stack1,stack2 = [],[]
        p,q = pHead1,pHead2

        while p :
            stack1.append(p)
            p = p.next

        while q:
            stack2.append(q)
            q = q.next

        last_node = None
        while stack1 and stack2:

            node1,node2 = stack1.pop(),stack2.pop()

            if node1 != node2:
                return last_node

            last_node = node1

