
"""
my solution:
循环查找差是否在list里面。
执行用时 :
1200 ms
, 在所有Python3提交中击败了
35.59%
的用户
内存消耗 :
13.5 MB
, 在所有Python3提交中击败了
96.32%
的用户
时间复杂度 On2 空间复杂度 O1
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,num in enumerate(nums):
            if target - num in nums and nums.index(target-num) != idx:
                return [idx,nums.index(target-num)]

"""
看到别人的思路，顺手实现了一下，大概就是用hashmap（dic）来存储
时间复杂度 o(n) 空间复杂度o(n)
执行用时 :
88 ms
, 在所有Python3提交中击败了
50.57%
的用户
内存消耗 :
14.7 MB
, 在所有Python3提交中击败了
7.59%
的用户
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for idx,num in enumerate(nums):
            if target - num in dic and nums.index(target-num) != idx:
                return [idx,nums.index(target-num)]
