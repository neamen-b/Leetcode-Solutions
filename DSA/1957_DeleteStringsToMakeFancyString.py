# THis is a hashmap approach that almost worked but failed beacause I cannot handle consecutive letters only

class Solution:
    def makeFancyString(self, s: str) -> str:

        mydic = {}
        other_str = []

        for index, char in enumerate(s):
            if char in mydic.keys():
                mydic[char] +=1
            else:
                mydic[char] = 1
            
            if mydic[char] <= 2:
                other_str.append(char)
            else:
                mydic[char] = 0
            
        return ''.join(other_str)

    
sol = Solution() 
# print(sol.makeFancyString("aaabaaaa"))


# second attemps
class Solution2:

    def makeFancyString2(self, s: str) -> str:
        return_str = []
        return_str.append(s[0])
        consecutive_count = 1

        for i in range(1, len(s) - 1):

            if s[i] == s[i - 1]:
                consecutive_count+=1

            else:
                consecutive_count = 1

            if consecutive_count <= 2:
                return_str.append(s[i])

        return return_str

sol = Solution2()
print(sol.makeFancyString2("leeetcode"))