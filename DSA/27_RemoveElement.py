from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # To keep track of values not equal to val
        len_of_nums = len(nums)

        # In case nums is empty
        if nums is []:
            return 0

        # Go through nums and replace each occurence of val with -1
        # and update the length of nums considering non val values
        for i in range(len(nums)):
        
            if nums[i] == val:
                len_of_nums-=1
                nums[i] = -1

        # Sort in reverse becasue vals were replaced by -1
        nums.sort(reverse=True)
        return len_of_nums

# order O(n logn) at best
# Slowest part is the sort