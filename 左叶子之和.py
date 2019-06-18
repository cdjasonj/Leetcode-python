'''
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-left-leaves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#直接判断左节点是否是叶子。
class Solution:
    sum = 0
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left:
            node = root.left
            if not node.left and not node.right: #如果左节点是叶子节点
                self.sum += node.val
            self.sumOfLeftLeaves(root.left)
        if root.right:
            self.sumOfLeftLeaves(root.right)
        return self.sum