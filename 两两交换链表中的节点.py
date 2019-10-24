# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""

给定 1->2->3->4, 你应该返回 2->1->4->3.

p,q 节点，每次 遍历两个节点
"""

class Solution:
    def swapPairs(self, head):
        pre = List_Node(0)
        pre.next = head
        temp = pre

        while temp.next and temp.next.next:
            start = temp.next
            end = temp.next.next
            temp.next = end
            start.next = end.next
            end.next = start
            temp = start
        return pre.next
