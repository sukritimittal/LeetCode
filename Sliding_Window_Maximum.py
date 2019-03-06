#Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

#Example:

#Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
#Output: [3,3,5,5,6,7] 
#Explanation: 

#Window position                Max
#---------------               -----
#[1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = []
        if (nums != []):
            for i in range((len(nums)) - k + 1):
                # window = []
                if i == 0:
                    for j in range(k):
                        window.append(nums[i+j])
                else:
                    window.remove(nums[i-1])
                    window.append(nums[i+k - 1])
                result.append(max(window))
        return result
