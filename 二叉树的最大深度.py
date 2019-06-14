'''
最近提交结果：
通过
显示详情
执行用时 :
56 ms
, 在所有Python3提交中击败了
98.34%
的用户
内存消耗 :
14.9 MB
, 在所有Python3提交中击败了
86.22%
的用户
炫耀一下:
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            left_deep = self.maxDepth(root.left)
            right_deep = self.maxDepth(root.right)
            return max([left_deep,right_deep])+ 1
        else:
            return 0