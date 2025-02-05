class Solution:
    def lengthOfLastWord(s: str) -> int:
        split = s.split(" ")
        return (len(split.pop()))
    
    
    
    
    
    
"""1. Start from the back
    2. If whitespace, ignore
    3. else, count until you see the next whitespace """
    
    
    # def SecondMethod(s:str) -> int:
        
    #     change_white_space = 0
    #     letter_count = 0
    #     previous_character = None

    #     for i in range(len(s)-1 ,0 ,-1):

    #         if(s[i] != previous_character):
    #             change_white_space+=1
    #             previous_character = s[i]
    #             print(f"prev {previous_character}, change {change_white_space}")
    #         if (s[i] != " " and change_white_space<=1):
    #             letter_count =+ 1

    #     return letter_count


        

    