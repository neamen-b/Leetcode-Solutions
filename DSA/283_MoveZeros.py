from typing import List
def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        keep track of the earliest zero
        everytime you see a natural number, swap with the earliest zero
        update the earliers zero pointer by one
        however this means that earliest could point to a non-zero
        """

        earliest_zero, i = 0, 0

        while i < len(nums):
            if nums[i] != 0:
                if earliest_zero != i:
                    nums[earliest_zero], nums[i] = nums[i], nums[earliest_zero]
                    # print(f"non zero, {earliest_zero}")
                earliest_zero += 1
            i += 1