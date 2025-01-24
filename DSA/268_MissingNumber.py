      #Initial thoughts
  #two for loops
        #Sum up number from 0-n in the first loop
        # sum up numbers in array nums
        # if sum1 = sum2 return. All there
        #else return abs(sum1-sum2)

        #If the difference is Zero this won't work 
        # How do I fix this without hard-coding it?

        #Just return the abs of the difference instead

from typing import List
def missingNumber(nums: List[int]) -> int:

        array_sum = sum(nums)
        # print(a)
        size = len(nums)
        sum_zero_to_n = 0

        for i in range(size + 1):
            sum_zero_to_n+=i
        
            return abs(array_sum-sum_zero_to_n)

        
print(missingNumber([1]))