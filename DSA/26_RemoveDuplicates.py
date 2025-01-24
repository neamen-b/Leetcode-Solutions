from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        myset = set()

        for i in range(len(nums)):

            if nums[i] not in myset:
                myset.add(nums[i])
            else:
                nums[i] = float("-inf")        
        nums = nums.sort()
        return len(myset)

