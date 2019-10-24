"""

只要是logn的查找算法

1，利用二分查找找出 rotation_index
2，在根据查找出来的结果，决定查找区间，再使用二分查找
"""

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        def find_rotation_index(left,right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                mid = (left+right)//2
                if nums[mid] > nums[mid+1]:
                    return mid + 1
                if nums[mid] < nums[left]:
                    right = mid -1
                else:
                    left = mid +1

        def binary_search(left,right):

            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return -1
        if nums[0] < nums[-1]:
            return binary_search(0,len(nums)-1)

        rotation_index = find_rotation_index(0,len(nums)-1)
        print(rotation_index)
        if target < nums[0]:
            return binary_search(rotation_index,len(nums)-1)
        else:
            return binary_search(0,rotation_index-1)

S = Solution()
print(S.search([4,5,1,2,3],1))