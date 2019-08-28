#:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)


#返回连续子向量的最大和

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here

        sum = array[0]
        max = array[0]

        for num in array:

            if sum < 0:

                sum = num

            else:

                sum += num

            if sum > max:
                max = sum
        return max