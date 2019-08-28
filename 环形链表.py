"""

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

#方法1， hashset
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashset = set()

        p = head
        while p :

            if p not in hashset:
                hashset.add(p)
                p = p.next
            else:
                return True

        return False

#方法2 ，快慢表
"""

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# 方法2, 快慢表，   一个指针一次遍历两个node,一个指针一次遍历一个node 

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #用两个指针遍历链表
        p1 = head.next
        p2 = head

        step = 0
        while p1 and p2 :

            if step == 2:
                p2 = p2.next
                step = 0

            p1 = p1.next
            step += 1

            if p1 == p2:
                return True


        return False