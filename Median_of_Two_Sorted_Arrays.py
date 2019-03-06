#There are two sorted arrays nums1 and nums2 of size m and n respectively.

#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

#You may assume nums1 and nums2 cannot be both empty.

#Example 1:

#nums1 = [1, 3]
#nums2 = [2]

#The median is 2.0

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = 0
        nums1 = sorted(nums1 + nums2)
        leng = len(nums1)
        
        if leng%2 == 0:
            result = (nums1[int(leng/2) - 1] + nums1[int((leng)/2)  + 1 - 1])/2
        else:
            result = nums1[int((leng+1)/2) - 1]
        
        return result
        
