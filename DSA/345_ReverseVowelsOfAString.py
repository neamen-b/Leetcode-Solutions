'''
Initial thoughts

    step 1 -
        find all vowels. helper funciton to tell you if it is in
            implement a hashset with the vowels lower and upper case

    step 2 :
        add those vowels to a string and sort 
            this will make it an nlogn solution
            no need to worry about tie breakers (stability)
            question does not specify what to do
        if consonant add to ans list at same index
    step 3:
        go through ans list (which should)
            if not const:
                add from vowel

    order:
        O(n) - time
        O( len(vowels) + len(s))


    problem:
        s include all printable ASCII characters INCLUDING " ", which messes with your solution
        if there is a space in s, it going to be replaced by vowels when the last for loop checks if element
        is " "

    solution:
        no need for an array initialized to " "
        just turn s into a list and then replace vowels with the new order of vowels
        This is implemented in reverseVowels2
    s 
'''

class Solution:

    def reverseVowels(s: str) -> str:
        # initialize set with vowels for O(1) look up. Space comp O(len(vowels in s))
        vowels = {'a','i','e','o','u','A','E','I','O','U'}
        ans = [' ' for _ in range(len(s))]
        sorted_vowels = []

        for index, char in enumerate(s):
            if char in vowels:
                sorted_vowels.append(char)
            else:
                ans[index] = char
        # print(ans)
        sorted_vowels.reverse()
        # print(sorted_vowels)
        v_count = 0
        i = 0
        while v_count < len(sorted_vowels):
            if ans[i] in vowels:
                # print(ans[i])
                ans[i] = sorted_vowels[v_count]
                v_count += 1
            i += 1
            
        return ''.join(ans)

    def reverseVowels2(s: str) -> str:
        vowels = {'a','i','e','o','u','A','E','I','O','U'}
        # O (n) time and O(n) space where n  = len(s)
        ans = list(s)
        sorted_vowels = []

        for index, char in enumerate(s):
            if char in vowels:
                sorted_vowels.append(char)

        # print(ans)
        sorted_vowels.reverse()
        # print(sorted_vowels)
        v_count = 0
        i = 0
        while v_count < len(sorted_vowels):
            if ans[i] in vowels:
                # print(ans[i])
                ans[i] = sorted_vowels[v_count]
                v_count += 1
            i += 1
            
        return ''.join(ans)        
    
ans = Solution.reverseVowels2("IceCreAm")
print(ans)



        


