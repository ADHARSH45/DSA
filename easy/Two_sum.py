from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int):
        
        indx = {}
        for i in range(len(nums)):
            indx[nums[i]] = i
        for i in range(len(nums)):
            a = target - nums[i]
            if a in indx and indx[a] != i:
                return [i,indx[a]]

"""
Problem to find wheter there exist two numbers that sums upto the target it can be done using hashmap and the compliment.

"""