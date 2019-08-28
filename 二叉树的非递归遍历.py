
""""

class TreeNode():
    def __init__(x):
        self.val = x
        self.left = None
        self.right=  None
"""


def LevelOrder(root):

    if root:
        queeue = [root]
        result = []
        while queeue:
            next_layer_queeue = []
            layer = []
            for node in queeue:
                layer.append(node.val)
                for child in node:
                    next_layer_queeue.append(child)
            result.append(layer)
            queeue = next_layer_queeue

def PreOrder(root):
    #用栈就解决了
    stack = []
    result = []
    if root:
        stack.append(root)

        while stack:
            node = stack.pop() #栈尾节点出栈
            result.append(node.val)
            if node.right :
                stack.append(node.right) #右孩子先进栈
            if node.left:
                stack.append(node.left) #左还子后进栈

def InOrder(root):
    # 将一节点的左下节点全部入栈，再扫描右节点，让右孩子节点的所有左节点入栈
    stack = []
    result = []
    if root:
        p = root
        while p or stack :

            # 将左下节点全部入栈
            while p :
                stack.append(p)
                p = p.left

            if stack:
                p = stack.pop()
                result.append(p.val)
                p = p.right


