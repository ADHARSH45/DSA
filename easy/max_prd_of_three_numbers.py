class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        val1 = nums[-1] * nums[-2] * nums[-3]
        val2 = nums[0] * nums[1] * nums[-1]
        return max(val1,val2)
      
"""
Here given an array of integers find the maximum product of any three numbers .
"""
