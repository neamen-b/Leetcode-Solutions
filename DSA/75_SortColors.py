'''
Initial thoughts:
    1. Tough one. After doing research on sorting algorithms, found the Dutch National Flag by good ol' Dijkstra
        essentially grouping values but in order

        If you find '0' in the middle, swap it with the first element
        If you find '1' in the middle, it is where it belongs
        If you find '2' in the middle, swap it with the last element

        Now this mean that this sort is not stable. 

        So after swapping, we need to upadte the pointers beacuse we don't want them to point elements
        that are already in the right location. 

        If 0, increase start by 1 because the next 0 would be placed right after the one already placed
                also increase mid look at the next element

                # Just realized that mid is a misleading term, should be called index or just pointer
        If 1, then leave it there and update to pointer to the next index

        If 2, decrease end by 1 because the next 2 would be placed just before the last element which should be
            in the last position

                ** Correction. DO NOT INCREMENET MID because what swapped with end still needs to be checked.

'''

from typing import List

class Solution:

    def sortColors(self, nums: List[int]) -> None:
        
        # points to beginning of unsorted array
        start = 0
        # Used to traverse the whole array nums
        iterator = 0

        # points to the ending of the unsorted array
        end = len(nums) - 1

        # start and end change because the unsorted region of the array narrows after
        # each iteration

        '''
        Example
        nums = 
            Original = |2|0|2|1|1|0|        start = 0 , iterator = 0 , end = 5  # No swaps
            Iterator(0) = |0|0|2|1|1|2|     start = 0 , iterator = 0 , end = 4  # 0,5 = 5,0
            Iterator(0) = |0|0|2|1|1|2|     start = 1 , iterator = 1 , end = 4  # 0,1 = 1,0 - 0 swapped 0 so no vsible difference
            Iterator(1) = |0|0|1|1|2|2|     start = 2,  iterator = 2,  end = 4  # 1,0 = 0,1 
            Iterator(2) = |0|0|1|1|2|2|     start = 2,  iterator = 2,  end = 3  # No swaps, leave 1
            Iterator(3) = |0|0|1|1|2|2|     start = 2,  iterator = 3,  end = 3  # No swaps, leave 1
            Iterator(4) = |0|0|1|1|2|2|     start = 2,  iterator = 4,  end = 3

            Loop ends becuase iterator = 4 and end = 3, the unsorted part is gone essentially
        '''
        # If iterator > end, then both halves of nums has elements in their right location
        while iterator <= end:
            
            # If iterator is
            if nums[iterator] == 0:
                nums[start], nums[iterator] = nums[iterator], nums[start]
                start+=1 ; iterator+=1
            
            elif nums[iterator] == 1:
                iterator+=1

            elif nums[iterator] == 2:
                nums[end], nums[iterator] = nums[iterator], nums[end]
                end-=1

            # Felt bad ending on a elif
            else:
                pass
        
            print(nums)
            print(start , iterator, end)
        # return nums


sol = Solution()
print(sol.sortColors([2,0,2,1,1,0]))