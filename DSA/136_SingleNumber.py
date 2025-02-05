
# Thoughts
'''
Iterate over and add to a set if it is not already in there. 
So if a number repeats, it won't be added, and the only number added will the single one

Problems?
a.  Lookup is O(1)
    Adding is O(1)

    complexity just O(n) for lopp to iterate through the List

b. The first element will be added. It could be the single or not. 
    So if seen again, remove from set. This will only apply to the first element if it is not single
'''
from typing import List
class solution:

    def singleNumber (self, nums: List[int]) -> int:

        # set to keep track of numbers seen
        myset = set()

        # Go through each number in nums
        for number in nums:
            # print(f"myset {myset} at {number}")

            # Remove from set if inside
            if number in myset:
                myset.remove(number)
            # else add ot to set
            else:
                myset.add(number)
        
        # Return the element left in myset
        return myset.pop()
    

sol = solution()
answer = sol.singleNumber([4,1,2,1,2])

print(f"Single Element: {answer}")


            



