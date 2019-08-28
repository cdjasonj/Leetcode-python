"""

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

"""


class Solution:
    def isSymmetrical(self, pRoot):
# write code here

        #循环判断左子树的根节点和右子树的根节点的值是否相同

        if not pRoot:
            return True

        else:
            return self._isSymmetrical(pRoot.left,pRoot.right)
    def _isSymmetrical(self,left,right):

        if not left and not right:
            return True

        elif not left :
            return False

        elif not right:
            return False

        return left.val == right.val & self._isSymmetrical(left.left,left.right) & self._isSymmetrical(right.left,right.right)

