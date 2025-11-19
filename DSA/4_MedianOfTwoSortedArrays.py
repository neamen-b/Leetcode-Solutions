# Merge the two arrays then find the median
from typing import List 

class Solution:

    def merge(self, nums1 : List[int], nums2 : List[int]) -> List[int]:
        nums1Size, nums2Size = len(nums1), len(nums2)
        if (nums1Size + nums2Size == 0): return nums1

        newList = []
        index_1, index_2 = 0 ,0

        while(index_1 < nums1Size and index_2 < nums2Size):

            if(nums1[index_1] <= nums2[index_2]):
                newList.append(nums1[index_1])
                index_1 += 1
            else:
                newList.append(nums2[index_2])
                index_2 += 1

        while(index_1 < nums1Size):
            newList.append(nums1[index_1])
            index_1 += 1

        while(index_2 < nums2Size):
            newList.append(nums2[index_2])
            index_2 += 1

        # print(index_1, index_2, newList)
        
        return newList

    def findMedian(self, nums1: List[int], nums2 : List[int]) -> float:

        merged_vec = self.merge(nums1, nums2)
        median = 0.0
        # Subtract 1 because it is xero indexed
        median_index = ((len(merged_vec) + 1) // 2) - 1

        # Odd length
        if (len(merged_vec) % 2 != 0):
            median = merged_vec[median_index]
        # Even length
        else:
            median = (merged_vec[median_index] + merged_vec[median_index + 1]) / 2
        
        return median


obj = Solution()
print(f"median = {obj.findMedian([1,2,3], [4,5,9])}")
            

