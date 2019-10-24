# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return None

        new_head = ListNode(0)
        new_head.next = head

        #首先先求出链表的长度
        length = self.get_list_length(head)
        #k有效部分
        k = k % length
        for i in range(k):
            q = new_head.next
            last_val = q.val
            q = q.next
            while q:
                temp = q.val
                q.val = last_val
                last_val = temp
                q = q.next
            new_head.next.val = last_val

        return new_head.next

    def get_list_length(self,head):

        length = 0
        q = head
        while q:
            length+=1
            q = q.next
        return length