import math


class Solution(object):
    def nextPermutation(self, nums):
        for i in range(len(nums)-1, 0, -1):
            # find the index of the last peak
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                j = i - 1
                for k in range(i, len(nums)):
                    if nums[j] < nums[k]:
                        nums[k], nums[j] = nums[j], nums[k]
                        return nums
        return nums.reverse()
