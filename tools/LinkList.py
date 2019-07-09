class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def Create_LinkList(list_data):
    head = Node(0)
    p = head
    for data in list_data:
        temp = Node(data)
        p.next = temp
        p = p.next
    return head

def Print_LinkList(ListNode):

    list = []
    while ListNode:
        list.append(ListNode.val)
        ListNode = ListNode.next
    print(list)