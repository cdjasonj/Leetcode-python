'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#注意删除节点一定要构造一个头节点，不然第一个没法删
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 用一个记录他的倒数N个节点的前面节点，然后删除
        new_head = ListNode(0)  # 要有一个头节点，不然第一个删不了
        new_head.next = head
        num = 1
        p = head
        while p and num < n:  # 找到他的前面一个节点
            p = p.next
            num += 1
        del_pr = new_head
        while p.next:  # 到达最后一个节点
            del_pr = del_pr.next
            p = p.next
        del_pr.next = del_pr.next.next

        return new_head.next

