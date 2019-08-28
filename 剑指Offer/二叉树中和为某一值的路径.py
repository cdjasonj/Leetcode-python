"""
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):


        ret = []
        path = []

        if not root:
            return []

        self._find(root,expectNumber,ret,path)
        return ret

    def _find(self,root,target,ret,path):

        #节点为空， 回溯
        if not root:
            return

        #节点为叶子节点，且满足路径条件
        if not root.left and not root.right and root.val == target:
            #ret添加路径
            ret.append(path[:])

        #遍历左节点
        if root.left:

            self._find(root,target - root.val,ret,path)

        if root.right:

            self._find(root,target - root.val, ret, path)

        #路径回溯， 遍历另外一个子树
        path.pop()