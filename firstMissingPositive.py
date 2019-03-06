#Given an unsorted integer array, find the smallest missing positive integer.

#Example 1:

#Input: [1,2,0]
#Output: 3

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result = 0
        if nums == [] or max(nums) <1:
            return 1
        for i in range(1, max(nums)):
            if i not in nums:
                return i
        if result == 0:
            result  = max(nums) + 1
        return result
                
