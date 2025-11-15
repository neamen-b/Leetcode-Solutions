# Let's pradctice crearting substrings

from typing import Optional, List, Set
from collections import Counter
import math


class Solution:

    def createSubstring(self, inputString : str) -> List[str]:
        
        subStrings : List[str] = []

        for i in range(len(inputString)):
            for j in range(i , len(inputString)):
                subStrings.append(inputString[i:j + 1])
        
        return subStrings
    

    # Depending on the argument 'repeating', can find longest repeating or nonrepeating substring
    # Defaults to nonrepeating
    def longestSubstring(self, substrings : List[str], repeating = False) -> int:
        maxLength = 0

        # Looking for the largest substring with repeating characters
        if repeating: 
            for sub in substrings:
                start, end, validSub = 0, len(sub) - 1, True
                while(start < end and validSub):

                    if(sub[start] == sub[end]):
                        end -= 1
                    else:
                        validSub = False
                
                if validSub:
                    maxLength = len(sub) if len(sub) > maxLength else maxLength

        # Looking for the largest substring with nonrepeating characters
        else:
            for sub in substrings:
                characterCount = Counter(sub)
                # If there are x number of letters that don't repeat, the sum of count should be x 

                # O(len(character.values()))
                if len(characterCount) == sum(characterCount.values()):
                    maxLength = len(sub) if len(sub) > maxLength else maxLength
        
        return maxLength
    
    # Use two pointers to go through string s
    # start = 0, end = 0
    # is s[start] != s[end]: end++ else
    
    def twoPointerMethod(self, s : str) -> int:
        validWindow : Set[str]= set()
        start, end = 0, 0
        maxLength : int = 0

        
        while end < len(s):
            
            print(f"start of iteration : window = {validWindow}, start {start}, end {end}")
            if s[end] not in validWindow:
                validWindow.add(s[end])
                end += 1
            else:
                validWindow.remove(s[start])
                start += 1

            maxLength = max(maxLength, len(validWindow))
            print(f"end of iteration: window = {validWindow}, start {start}, end {end} \n ------------------------------------------")
        return maxLength


                    


obj = Solution()
substrings = obj.createSubstring("abcabcbb")
maxSubstring = obj.longestSubstring(substrings)
print(obj.twoPointerMethod(" "))


