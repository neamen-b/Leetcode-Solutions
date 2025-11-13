

# Does not work becuase when popping you could remove the count of a number which is still in the window. 
def largestInteger(nums, k: int) -> int:
        missing_number = float("-inf")
        # Window size is k. find the a unque number in that window
        mymap = {}
        window = 1
        for i in range(k):
            if nums[i] in mymap:
                mymap[nums[i]] = mymap.get(nums[i]) + 1
            else:
                mymap[nums[i]] = 1
        
        for i in range(len(nums)):
            if mymap[nums[i]] == 1:
                missing_number = max(missing_number, mymap[nums[i]])
            if window == k:
                pop = window - i - 1
                mymap.pop(mymap[nums[pop]])
                if i + 1 < len(nums):
                    if nums[i + 1] in mymap:
                         mymap[nums + 1] += 1
                    else:
                        mymap[nums[i + 1]] = 1


        
                    
            

