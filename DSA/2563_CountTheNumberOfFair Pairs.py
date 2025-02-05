
'''
initial thoughts
Two pointers:

    i,j=0,len(nums)-1
    count = 0

    sort num then 
    while i <j:
        
        if lower < sum < upper:
            count pairs in between
            count += j-1
        elif lower > sum < upper:
            i++, move up from right
        elif lower < sum >upper:
            j--, move down from left
'''
from typing import List
def CountFairPairs(nums: List[int], lower: int, upper: int)-> int:
    count, i, j = 0, 0, len(nums)-1
    nums.sort()
    # print(nums)
    while i < j:

        # print(i,j)
        if (nums[i]+nums[j]) < lower:
            i+=1
        elif (nums[i]+nums[j]) > upper:
            j-=1
        elif (nums[i]+nums[j])  >= lower and (nums[i]+nums[j]) <= upper:
            k,m=i,j

            # Once in that window where the sums are GUARANTEED to be less || = than upper
            # Starting from the right, keep going down while the sums are >=lower, increasing count. 
            # if the number to the immediate of index j does not cut it, break since the rest won't. 
            # problem here is if it keeps going, i.e. the numbers at indices to the left j keep meeting test. 
            # This gets really slow but works. 
            while k < m:
                if(nums[k]+nums[m]>=lower):
                    # print("here")
                    count+=1
                    m-=1
                else:
                    break
            i+=1
    return count 

# print(CountFairPairs([0,1,7,4,4,5],3,6))

# for i in range(10):
#     i+=1
#     print(i,j)



'''
Attempt two:
    The problem is that I cannot guarantee that the window the above code provides contains
    numbers that can sum with nums[i] to be >= lower. What to do ?

    Eureka! If the number to the immediate right of i + nums[i] < lower then the rest won't work
    False Eureka

    How about implementing Binary Search find where (nums[i] - lower) would go in sorted nums
    Then indices to the right of the placement meet the requirement while indices to the left don't


'''

def CountFairPairs2(nums: List[int], lower: int, upper: int) -> int:
    count, i, j = 0, 0, len(nums)-1
    nums.sort()
    # print(nums)
    while i < j:

        # print(i,j)
        if (nums[i]+nums[j]) < lower:
            i+=1
        elif (nums[i]+nums[j]) > upper:
            j-=1
        else:
            start, end, tgt, pos = i+1,j,lower-nums[i],0

            # print(start, end, tgt)
            while start < end:
                print(nums[start:end+1])
                mid = (start + end)//2
                if nums[i] + nums[mid] < lower:
                    start = mid + 1
                # print(start, end, mid, nums[mid])
                else:
                    end = mid
                    # print("insertion = ", mid)
            if (nums[i]+nums[start])  >= lower and (nums[i]+nums[start]) <= upper:
                print(start, end, mid, nums[mid])
                print("----------")
            # pos = mid + 1
                count +=abs(j-start+1)
            i+=1
    print(count)
    return count 

CountFairPairs2([0,1,7,4,4,5],3,6)

# sgr = [1,2,3,4]
# print(sgr[0:3])


# Binary Search

def BinarySearch(nums, tgt):
    start, end , insert_position= 0, len(nums)-1,0


    while start <= end:
        mid = (start + end)//2
        print(mid)
        if tgt == nums[mid]:
            return mid
        elif tgt > nums[mid]:
            start = mid + 1
        else:
            end = mid
    return mid + 1

# print(BinarySearch([0,0,0,0,],1))
