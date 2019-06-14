'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

''''
最近提交结果：
通过
显示详情 
执行用时 :
64 ms
, 在所有Python3提交中击败了
89.22%
的用户
内存消耗 :
13 MB
, 在所有Python3提交中击败了
94.99%
的用户
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next:
            if p.next.val == p.val:
                self.del_node(p)
            p = p.next
        return head

    def del_node(self, head):
        # 找到第一个val != head.val
        temp = head
        while temp and temp.val == head.val:
            temp = temp.next
        head.next = temp
