"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
"""


"""
思路， 输入序列的最后一个是根节点， 那么找到， 左子树元素 ，右子树元素，
"""


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here

        if not sequence :
            return False


        return self._VerifySquenceOfBST(sequence,0,len(sequence) - 1)


    def _VerifySquenceOfBST(self,sequence,start,end):

        i , j = 0,0

        if start >= end:
            return True


        root_node = sequence[end] #当前子树的根元素

        for i in range(0,len(sequence)-1):

            if sequence[i] > root_node:
                break #找到划分点

        for j in range(i,len(sequence)) :

            if sequence[j] < root_node:

                return False

        right,left = True,True

        if i > start:

            left = self._VerifySquenceOfBST(sequence,start,i-1)

        if j < end:

            right = self._VerifySquenceOfBST(sequence,i,end)

        return left and right
