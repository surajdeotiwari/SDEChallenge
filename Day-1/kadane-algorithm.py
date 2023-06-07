class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use of Kadane Algorithm
        current_max_sum = nums[0]
        final_max_sum = nums[0]
        for i in range(1, len(nums)):
            current_max_sum = max(nums[i], current_max_sum+nums[i])
            final_max_sum = max(current_max_sum, final_max_sum)
        return final_max_sum
