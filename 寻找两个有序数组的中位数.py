"""

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

"""
import math

#1，先判断 有序数组的合并的长度是奇数还是偶数， 奇数则是 math.ceil(len(list)/2)  , 偶数是 len(list)/2, len(list)/2+1


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = self._mergeNums(nums1,nums2)

        if (len(nums1) + len(nums2)) %2  == 0 :

            mid_pos1 = int((len(nums1) + len(nums2)) / 2) - 1
            mid_pos2 = int((len(nums1) + len(nums2)) / 2 +1) - 1

            return (nums[mid_pos1]+nums[mid_pos2])/2
        else:
            mid_pos = int(math.ceil((len(nums1) + len(nums2)) / 2)) - 1

            return nums[mid_pos]

        #合并两个有序有序数组

    def _mergeNums(selfn,nums1,nums2):

        nums = []
        #首先判断中位数在哪儿
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while i < len(nums1):

            nums.append(nums1[i])
            i += 1

        while j < len(nums2):

            nums.append(nums2[j])
            j += 1
        return nums

s = Solution()
print(s.findMedianSortedArrays([],[1,2,3,4,5]))