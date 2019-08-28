
"""

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

"""

#判断链表是否有环 1, 快慢指针， 2， 用hash表存储， 遍历到第一个重复的节点的前一个节点就是环的入口

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        node_set = set()
        p = pHead
        last_node = None
        while p :
            if p in node_set:
                return last_node

            else:
                node_set.add(p)
                last_node = p
                p = p.next

        return None
