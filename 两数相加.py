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

#没刷出来，之后再刷，刚开始刷有点手生

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#这个超时了
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = self.get_num(l1) + self.get_num(l2)
        # 创建头链表
        l3 = ListNode(x % 10)
        x %= 10
        while x:
            temp = ListNode(x % 10)
            l3.next = temp
            l3 = temp
            x %= 10
        return

    def get_num(self, l_node):
        num = 0
        temp = 1
        while l_node:
            num += l_node.val * temp
            temp *= 10
            l_node = l_node.next
        return num

#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        p1, p2 = l1, l2

        flag = 0  # 用一个flag 来判断进位
        num1, num2 = p1.val, p2.val
        if val >= 10:
            val = (num1 + num2) % 10 + flag
        flag = 1
        else:
        val = (num1 + num2)

    # 创造头节点
    l3 = ListNode(val)
    p2, p1 = p1.next, p2.next
    p = l3
    while p1 and p2:

        num1, num2 = p1.val, p2.val
        val = num1 + num2 + flag
        if val >= 10:
            flag = 1
            val = val % 10
        else:
            val = (num1 + num2)

        p.next = ListNode(val)
        p = p.next
        p1, p2 = p1.next, p2.next

    # 最高为进位判断
    if flag != 0:
        p.next = ListNode(flag)
        p = p.next

    while p1:
        p.next = ListNode(p1.val)
        p = p.next
        p1 = p1.next

    while p2:
        p.next = ListNode(p2.val)
        p = p.next
        p2 = p2.next

    return l3