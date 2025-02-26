'''
Initial thoughts

    initialize set with vowels
    iterate through sting if xhar in set, start a counter, 
    if you encouner a consonant, clear counter
    if counter > max set set to counter

    actually no, I misundetstoof the question
'''

def maxVowels(s, k):

    max_vowels = float("-inf")
    vowels_count = 0
    vowels = set(['a','e','i','o','u'])

    for i in range(k):
        if s[i] in vowels:
            vowels_count += 1
    max_vowels = max (max_vowels, vowels_count)
    print(f"pre vcount = {vowels_count}, max = {max_vowels}")
    i = 0
    j = i + k

    while j < len(s):
        print(f"{s[i:j + 1]}")
        if s[i] in vowels:
            vowels_count -= 1
        
        if s[j] in vowels:
            vowels_count += 1

        print(f"vowel count = {vowels_count}")
        max_vowels = max (max_vowels, vowels_count)
        i += 1
        j += 1

    return max_vowels

# print(maxVowels(s = "abciiidef", k = 3))


#There is a way to do this without the first loop though
# Turned out to be worse in terms of run time
def maxVowels2(s, k):

    i, j, vowel_count = 0, 0, 0
    vowels = {'a','e','i','o','u'}
    max_vowels = float('-inf')
    

    while j < len(s):

        if s[j] in vowels:
            vowel_count += 1
        
        # If the window size/ substring size has been reached
        if k == j - i + 1:
            max_vowels = max (max_vowels, vowel_count)
            # print(i , j, max_vowels)
            if s[i] in vowels:
                vowel_count -= 1
            
            i += 1
        j += 1
    return max_vowels

print(maxVowels2(s = "abciiidef", k = 3))