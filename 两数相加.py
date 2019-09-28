'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
my solution
"""

#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2 :
            return None
        p,q = l1,l2
        new_head = ListNode(0)
        n = new_head
        carry = 0
        while p or q:
            if p :
                num1 = p.val
                p = p.next
            else:
                num1 = 0

            if q :
                num2 = p.val
                q = q.next
            else:
                num2 = 0

            curr = (num1+num2+carry)%10
            carry = (num1+num2+carry)/10
            n.next = ListNode(curr)
            n = n.next

        if carry != 0 :
            n.next = ListNode(1)
            n = n.next
        return new_head.next

