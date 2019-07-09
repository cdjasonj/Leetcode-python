#用两个栈保存单链表，然后一一弹出，如果第一个不一样，那么他前一个就是公共链表.


def FindFirstCommonNode(head1,head2):
    p = head1.next
    q = head2.next

    stack1,stack2 = [],[]
    while p:
        stack1.append(p)
        p = p.next
    while q :
        stack2.append(q)
        q = q.next

    pr = stack1[-1]
    while stack1 and stack2:
        if stack1.pop() != stack2.pop():
            break
        else:
            pr = stack1.pop()
            stack2.pop()

    return pr