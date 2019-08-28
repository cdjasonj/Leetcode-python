class Solution:
    def search(self, nums: List[int], target: int) -> int:



    def _find_rotate_index(self,nums,left,right):
        #找到旋转index

        if nums[left] < nums[right]:
            return 0

        while left <= right:
            mid = (left+right) // 2
            pivot = nums[mid]
            if pivot > nums[left] : #左边有序
                left = mid + 1

            else:
