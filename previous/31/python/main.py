from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = N - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            # note 1. 两个判断条件写一行， 减少代码量
            # note 2. 判断条件是前者>=后者
            i -= 1
        # 通过判断避免单调递减的情况
        if i >= 0:
            j = N - 1
            while j >= 0 and nums[i] >= nums[j]:  # 注意判断条件
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i + 1, N - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
