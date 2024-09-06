'''
Initial thoughts:
    a. go through array and check if it element is in dictionary by key,
        if inside, add 1 to the value
        else, add to dictionary

        then, if element in dictionary.values() > n/2, get key at at that point

        if list(mydict.values()) has element > n/2 : return mydict.getkey(value)

    
    Execution
'''


from typing import List

class Solution():

    def majorityElement(self, nums : List[int]) -> int:

        # Dictionary to store element : count
        mydict = {}

        # Each element in nums
        for number in nums:
            
            # if not in mydict, add it with a count of one
            if number not in mydict:
                mydict[number] = 1
            
            # if in, increment count by 1
            else: 
                mydict[number] = mydict[number] + 1

        
        n = len(nums)
        
        # for each pair, see if count is > n/2, if so , return element
        for element, count in mydict.items():

            if count > (n/2):
                return element
            
        # Old approach
        # for count in list(mydict.values()):

        #     if count > (n/2):
        #         return mydict.ge
        


sol = Solution()

print(sol.majorityElement([3,2,3]))