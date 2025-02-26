'''
Initial thoughts
first finf the averga from 0 - k
    also find sum
then increment i, j 

while j < len(nums)
    avg = sum - nums[i] + nums[k] / k
    if avg < min then min = avg


    O(n)
'''

def findMaxAverage(nums, k):
    max_avg = float("-inf")
    sum = 0

    # If k == len(nums) then it is over there
    for i in range(k):
        sum += nums[i]
    max_avg = max(max_avg , sum / k)

    print(f"pre sum = {sum}, max_avg= {max_avg}")
    i = 0
    j = i + k

    while j < len(nums):
        sum -= nums[i]
        sum += nums[j]
        # print(i, nums[i], nums[j],  j, sum)
        max_avg = max (max_avg, sum / k)
        i += 1
        j += 1

    return max_avg
    
print(findMaxAverage([5], 1))