# Thought Process

'''
Input: string 

Process:
    1. remove all non-alpha numeric charachters
        a. Use the alphanumeric string fucntion
        b. Scratch that. isalphanum checks if it is alphanumeric not covert it
        c. So use regex and strip to 'clean' str (first convert to lower_case)
            1. regex: '0-9' & 'a-z' only
        d. Instead of strip, use findall (from re) to find only alpahnumeric characters

    2. Convert all uppercase characters to lowercase
        a. use to_lower function
    
    3. Use two pointers to make comparisons of corresponding indices of string
        a. i -> goes from the start , j -> goes from the end
        b. compare i and j, if not equal, then not palindrome
        c. Definition and limitation of i and j
            1. i goes up from 0 until (inclusive) len(s) // 2 (integer division)
            2. j goes down len(s) - 1  until (inclusive) len(s) // 2 (integer division)
    4. If s is empty, return True

Output: boolean

'''


import re 

class Solution:

    def isPalindrome(self, s: str) -> bool:
        
        # Empty string
        if s == '':
            return True
        
        # remove non_alphanumeric characters
        # Convert to lowercase first
        s = s.lower()

        # strip non-alphanumeric characters with regex expresion

        # This will be used as the preceding element for the findall funciton
        # a-z and 0-9
        pattern = r'[a-z0-9]'

        # Does three things
        matches = ''.join(re.findall(pattern= pattern, string = s))

        # The middle index with integer division
        mid_index = (len(matches)-1) // 2 

        # Python allowd for two sequences to be used simultaneously like Java
        # range(0, mid_index) populates 'i''s sequence
        # range(len(matches)-1, mid_index, -1) poopulates 'j's sequence
        # Zip puts those two sequence together. They should be equal given that s is split halfway
        for i, j in zip ( range(0, mid_index + 1), range(len(matches)-1, mid_index -1, -1)):
            
            print(f'matches at i {matches[i]}, matches at j {matches[j]}')
            print(f'j = {j} , i = {i}')
            if matches[i] != matches[j]:
                return False
        
        return True
                


sol = Solution()
print(sol.isPalindrome('race a car'))