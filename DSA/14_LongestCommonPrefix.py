from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #if Empty list
        if not strs:
             return ""

        # Find the smallest string based on length
        smallest = min(strs,key=len)
        
        #If smallest is empty string
        if smallest == "":
             return ""
        
        #collector or common prefix letters
        fin = []

        #The common prefix cannot be greater than the smallest string in strs
        for i in range(len(smallest)):
    
            for str in strs:
                    if str[i] == smallest[i]: 
                        let = smallest[i]
                        
                    else:
                        return ''.join(fin)
            fin.append(let)

        return ''.join(fin)