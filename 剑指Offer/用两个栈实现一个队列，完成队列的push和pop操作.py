"""

用两个栈实现队列

其实就是第二栈作为零时栈，  第一个栈元素全部出栈 push到 第二个栈， 这时候第二个栈元素出栈其实 就是队列的出队顺序
"""


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def push(self, node):

        return self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
