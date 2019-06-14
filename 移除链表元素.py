'''
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #思路，直接构造一个新的链表，不用删除
        new_head = ListNode(0)
        p = new_head
        while head:
            if head.val != val:
                p.next = head
                p = p.next
            head = head.next
        p.next = None #最后一定要将后面的节点置空，因为可能后面还有节点
        return new_head.next