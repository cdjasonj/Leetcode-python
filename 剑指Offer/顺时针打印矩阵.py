# -*- coding:utf-8 -*-

"""

需要注意的问题是他可能在循环当中已经出发结束条件了
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here

        result = []
        if matrix and matrix[0]:
            top_index = 0
            right_index = len(matrix[0]) - 1
            down_index = len(matrix) - 1
            left_index = 0

            while left_index <= right_index and top_index <= down_index:

                # 打印上边界, 从 left_index == > right_index

                if left_index <= right_index and top_index <= down_index:
                    index = left_index
                    while index <= right_index:
                        result.append(matrix[top_index][index])
                        index += 1

                    top_index += 1

                # 打印右边界， 从top_index ==> down_index
                if left_index <= right_index and top_index <= down_index:

                    index = top_index
                    while index <= down_index:
                        result.append(matrix[index][right_index])
                        index += 1

                    right_index -= 1

                # 打印下边界, 从right_index ==> left_index
                if left_index <= right_index and top_index <= down_index:
                    index = right_index
                    while index >= left_index:
                        result.append(matrix[down_index][index])
                        index -= 1

                    down_index -= 1
                # 打印左边界 从down_index ==> top_index
                if left_index <= right_index and top_index <= down_index:
                    index = down_index
                    while index >= top_index:
                        result.append(matrix[index][left_index])
                        index -= 1

                    left_index += 1

            return result