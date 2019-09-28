#动态规划

#初始化状态 f(n)=G,
#f(n-1) = G if arr[n-1] + n-1 >= len(status)-1 or status[arr[n-1] + n-1] = G
#f(n-1) = f(n-2) if arr[n-1] + n-1 < len(status)

#贪心，向后便利， 保存上一个能跳到最后的点
class Solution(object):
    def canJump(self, nums):

        if not nums :
            return False
        lastPosition = len(nums) - 1
        idx = len(nums) - 1
        while idx >= 0 :
            if nums[idx] + idx >= lastPosition:
                 lastPosition = idx
            idx -= 1

        return lastPosition == 0