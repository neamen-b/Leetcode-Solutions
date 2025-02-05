from typing import List

# Horribly slow solution. O(n^2)
def countPairs(nums: List[int], target: int)-> int:

    count = 0
    size = len(nums)

    for i in range(size):
        for j in range(i+1, size):
            if (int(nums[i]) + int(nums[j])) < target:
                count = count + 1
    
    return count

# print(countPairs([-6,2,5,-2,-7,-1,3], -2))
        

#Trying an O(nlogn) approach
def countPairs2(nums: List[int], target: int)->int:
    # count-> number of pairs, i,j-> pointers
    count, i, j = 0,0,len(nums)-1
    nums.sort()
    # print(nums)
    while i<j:
        if nums[i]+nums[j]<target:
            # print(j-i, "at",nums[i],nums[j])
            count+=(j-i)
            i+=1
        elif nums[i]+nums[j]>=target:
            j-=1
    return count

print(countPairs2([-1,1,2,3,1], 2))


