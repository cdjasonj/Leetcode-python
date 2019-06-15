'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
#超了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        num = 1
        p = head

        while p:
            if num == m - 1:  # 第一个节点的前一个节点当成头
                new_head = p
            elif num == n:
                new_head.next = p  # 最后节点接上n后面的节点
            else:
                p = p.next
                num += 1
        p = head
        while p:
            if num >= m and num <= n:  # 遍历到需要逆序的位置
                pr = p.next
                p.next = new_head.next
                new_head.next = p
                p = pr
                num += 1
            else:
                p = p.next
                num += 1
        return head

#关键在，怎么在一趟里面即找到要开始的节点，和剩下的节点的头节点 。