class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False

        return self.isSubTree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)

    def isSubTree(self,root1,root2):

        if not root2:
            return True

        if not root1:
            return False

        if root1.val == root2.val:

            return self.isSubTree(root1.left,root2.left) and self.isSubTree(root1.right,root2.right)
        return False

