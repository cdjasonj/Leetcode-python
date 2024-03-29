'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#注意使用头节点。 这种解法是原地的，时间复杂度是ON 空间复杂度是O1,没有额外空间创建
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p3 = head
        while l1 and l2:
            if l1.val < l2.val:
                p3.next = l1
                p3 = p3.next
                l1 = l1.next
            else:
                p3.next = l2
                p3 = p3.next
                l2 = l2.next
        while l1:
            p3.next = l1
            p3 = p3.next
            l1 = l1.next
        while l2:
            p3.next = l2
            p3 = p3.next
            l2 = l2.next
        return head.next