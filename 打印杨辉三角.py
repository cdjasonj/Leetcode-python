class Solution:
    def generate(self, numRows) :
        if not numRows :
            return []
        triangle = [[1]]

        for idx in range(1,numRows):
            temp = []
            temp.append(1)
            for col in range(len(triangle[idx-1])):
                if col == len(triangle[idx-1]) - 1: #遍历到上一行的最后一个
                    temp.append(triangle[idx-1][col])
                else:
                    temp.append(triangle[idx-1][col] + triangle[idx-1][col+1])
            triangle.append(temp)
        return triangle
S = Solution()
print(S.generate(5))