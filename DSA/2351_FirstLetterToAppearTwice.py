
'''
just count occurences and the first letter to hit 2 is the letter. 

'''
def repeatedCharacter(s: str) -> str:
        my_dic = {}

        for char in s:
            if char in my_dic:
                my_dic[char] += 1
                if my_dic[char] == 2:
                    return char
            else:
                my_dic[char] = 1
