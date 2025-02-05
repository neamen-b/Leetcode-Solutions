# intial thoughts
'''
    Double for-loop for O(n^2) solution
        for each value:
            for each other value
                if value = other value and index_of(value) != index_of(other value):
                    return nums.at_index(value)

        def findDuplicate(self, nums: List[int]) -> int:
            size = len(nums)
    
            for i in range(size):
                for j in range(size):
                    if nums[i]==nums[j] and i!=j:
                        return nums[i]
        This surpassed the time limit so no good


    Two pointer approach tortoise and hare
    forward movemnent with step k
    new idex = (i + k) % n, where n is the size of the array and i is the current index. 
    '''
from typing import List
#This does not work
def FindDuplicate(nums: List[int])-> int:
    size = len(nums)
    tortoise = 0
    hare = 0

    while tortoise <= size-1:
        print(f"tor {tortoise}, hare {hare}")
        tortoise = (tortoise + 1) % size
        hare = (hare + 2) % size
        if nums[tortoise] == nums[hare]:
            print(f"cycle detected. tor {tortoise}, hare {hare}")
            return nums[tortoise]

# print(FindDuplicate([18,13,14,17,9,19,7,17,4,6,17,5,11,10,2,15,8,12,16,17]))



# This one works
# Time complexity = O(n) Sapce Complexity = O(1)
def FindDuplicate2(nums: List[int])-> int:
    cycle = False
    tortoise = 0
    hare = 0

    while not cycle:
        # Tortoise make ones transition at a time while hare make two transitions at a time
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]

        print(f"Tortoise = {tortoise}, Hare = {hare}\nTor_node = {nums[tortoise]} hare_node = {nums[hare]}")
        if tortoise == hare:
            print(f"Tortoise = {tortoise} , Hare = {hare}")
            cycle = True

    tortoise = 0
    cycle_node_found = False
    while not cycle_node_found:
        tortoise = nums[tortoise]
        hare = nums[hare]

        if tortoise == hare:
            print(tortoise)
            cycle_node_found = True
            

FindDuplicate2([18,13,14,17,9,19,7,17,4,6,17,5,11,10,2,15,8,12,16,17])