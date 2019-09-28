"""


输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

"""


"""
思路:

对于前序遍历来说 每个遍历的都是根节点，
对于中序遍历来说，前序遍历的根节点左边的是左子树， 右边的是右子树


对于 前序遍历 1来说，  4，7，2 是左子树的中序遍历， 5，3，8，6 是右子树的中序遍历

                        2，4，7 是左子树的前序遍历， 3，5，6，8 是右数的前序遍历。 递归，
"""



class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here

        p_len = len(pre)
        t_len = len(tin)

        if p_len == 0 and t_len == 0:
            return None

        return  self.beConstruct(pre,tin,0,len(pre)-1,0,len(tin)-1)

    def beConstruct(self,per_list,tin_list,p_start,p_end,tin_start,tin_end):
        