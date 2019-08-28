# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#  直接递归判断左右子树的高度是否 > 1 就可以了 ，但是这种方法不是很好， 因为每个树节点会被反复遍历

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here

        if not pRoot:
            return True

        left_depth = self.treeDepth(pRoot.left)
        right_depth = self.treeDepth(pRoot.right)

        if abs(left_depth - right_depth) > 1:
            return False

        else:
            return self.IsBalanced_Solution(pRoot.left) & self.IsBalanced_Solution(pRoot.right)

    def treeDepth(self, root):

        if not root:
            return 0

        left_depth = self.treeDepth(root.left)
        right_depth = self.treeDepth(root.right)

        return max(left_depth, right_depth) + 1

