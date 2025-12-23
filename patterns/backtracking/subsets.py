from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index,curr):
            if index == len(nums):
                res.append(curr.copy())
                return 
            #print(index,res)
            backtrack(index + 1,curr)

            curr.append(nums[index])
            backtrack(index + 1,curr)

            curr.pop()
        backtrack(0,[])
        return res

obj  = Solution()
print(obj.subsets([1,2,3]))