# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#原地反转，关键在需要一个pr来保存下一个p在哪儿
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)
        p = head
        while p:
            pr = p.next
            p.next = new_head.next
            new_head.next = p
            p = pr
        return new_head.next